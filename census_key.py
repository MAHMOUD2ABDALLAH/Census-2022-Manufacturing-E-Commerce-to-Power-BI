import os
from pathlib import Path

def get_key():
    key = os.environ.get("CENSUS_KEY")
    if not key:
        env = Path(".env")
        if env.exists():
            for line in env.read_text().splitlines():
                line = line.strip()
                if line.startswith("CENSUS_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not key:
        key = input("Census API key: ").strip()
    return key