import os, requests, pandas as pd

BASE = "https://api.census.gov/data/2022/ecnecomm"
OUT = "output"
os.makedirs(OUT, exist_ok=True)

r = requests.get(BASE + "/groups.json", timeout=60)
r.raise_for_status()
d = r.json()

df = pd.DataFrame(d["groups"])
df.to_csv(f"{OUT}/groups.csv", index=False)
print("groups.py finished")