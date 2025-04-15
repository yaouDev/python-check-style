import os
import subprocess

result = subprocess.run(["flake8", "."], capture_output=True, text=True)

if result.returncode != 0:
    print("Style errors found:")
    print(result.stdout)
    exit(1)
else:
    print("No style errors found!")
    exit(0)