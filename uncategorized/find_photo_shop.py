import os
from pathlib import Path

ROOT = Path(r"C:\Users\melke\Documents")

for path in ROOT.rglob("**/*"):
    try:
        with open(path, "r", errors="ignore") as f:
            if "photoshop" in f.read():
                print(f.read())
    except PermissionError as e:
        print(path, e)

os.system("pause")