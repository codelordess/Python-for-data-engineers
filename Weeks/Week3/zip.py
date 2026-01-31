from pathlib import Path
from zipfile import ZipFile

with ZipFile('archive.zip', 'w') as zipf:
    for file_path in Path('data').rglob('*.*'):
        zipf.write(file_path, file_path.relative_to('data'))
