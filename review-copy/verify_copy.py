"""Read-only copy integrity check; does not review or regenerate the thesis."""
from pathlib import Path
import hashlib, json, re, urllib.parse, zipfile

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'review-copy'
rows = json.loads((AUDIT / 'source-files.json').read_text())
downloads = json.loads((AUDIT / 'drive-materials.json').read_text())
checkout_eol_extra = 0
for item in rows + downloads:
    path = ROOT / item['path']
    assert path.is_file(), item['path']
    raw = path.read_bytes()
    # The original .gitattributes explicitly requests CRLF for *.cmd. GitHub
    # archives and Git checkouts may materialize that inherited EOL conversion.
    # Verify the unchanged Git blob bytes without writing to the checkout.
    if item['path'] == 'server/mvnw.cmd' and b'\r\n' in raw:
        normalized = raw.replace(b'\r\n', b'\n')
        assert hashlib.sha256(normalized).hexdigest() == item['sha256']
        checkout_eol_extra += len(raw) - len(normalized)
        raw = normalized
    assert len(raw) == item['bytes'], item['path']
    assert hashlib.sha256(raw).hexdigest() == item['sha256'], item['path']
    if 'git_blob_sha' in item:
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == item['git_blob_sha'], item['path']

assert sum(x['path'].startswith('docs/materials/') for x in rows) == 20
for directory in ('server/', 'web/'):
    assert not any(x['path'].startswith(directory) for x in json.loads((AUDIT/'excluded-files.json').read_text())), directory

paper = ROOT / 'docs/thesis/毕业论文.md'
images = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', paper.read_text())
assert len(images) == 28
for image in images:
    assert (paper.parent/urllib.parse.unquote(image)).is_file(), image

paths = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts]
assert not any(p.is_symlink() for p in ROOT.rglob('*') if '.git' not in p.relative_to(ROOT).parts)
assert not any(p.suffix in ('.jar','.class') or p.name in ('.env','.gitmodules') for p in paths)
assert not any(b'version https://git-lfs.github.com/spec/v1' == p.read_bytes()[:42] for p in paths)
for p in paths:
    if p.suffix in ('.docx','.xlsx'):
        with zipfile.ZipFile(p) as z:
            assert z.testzip() is None, str(p)
    if p.suffix == '.pdf':
        raw = p.read_bytes()
        assert raw.startswith(b'%PDF-') and b'%%EOF' in raw[-2048:], str(p)
    assert not any(part in ('node_modules','__pycache__','target','.cache') for part in p.relative_to(ROOT).parts), str(p)

manifest = json.loads((AUDIT/'generated-files.json').read_text())
for item in manifest:
    assert hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest() == item['sha256'], item['path']
covered = {x['path'] for x in rows+downloads+manifest} | {'review-copy/generated-files.json','review-copy/verification-report.json'}
assert {str(p.relative_to(ROOT)) for p in paths} == covered, 'unmanifested or missing files'

size = sum(p.stat().st_size for p in paths)
assert size < 80_000_000 and len(paths) < 5_000
canonical_size = size - checkout_eol_extra
result = {'pass': True, 'files': len(paths), 'bytes': canonical_size, 'MB_decimal': round(canonical_size/1e6, 4), 'original_files_hash_verified': len(rows), 'original_materials_preserved': 20, 'drive_pdfs_hash_verified': len(downloads), 'thesis_image_references_resolved': len(images), 'old_history_included': False, 'gemini_actual_import_tested': False}
report = AUDIT/'verification-report.json'
if report.exists():
    saved = json.loads(report.read_text())
    assert all(saved[k] == result[k] for k in ('files','bytes','original_files_hash_verified','original_materials_preserved','drive_pdfs_hash_verified','thesis_image_references_resolved')), 'saved metrics differ'
print(json.dumps(result, ensure_ascii=False, indent=2))
if checkout_eol_extra:
    print('Inherited .gitattributes CRLF checkout conversion:', checkout_eol_extra, 'extra bytes; no file was rewritten.')
