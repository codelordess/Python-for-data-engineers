from pathlib import Path

path = Path('/Users/hephzibahemereole/Documents/Python Project/365DaysOfCode/Weeks/Week 2/tupule.py')
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.suffix)
path.mkdir()
path.rename('text.py')
print(path.stem)
print(path.parent)
path = path.with_name('text.txt')
path = path.with_suffix('.txt')
print(path)

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("**/*.py")]
print(py_files)