import os, requests, pandas as pd

BASE = "https://api.census.gov/data/2022/ecnecomm"
OUT = "output"
os.makedirs(OUT, exist_ok=True)

r = requests.get(BASE + "/groups/EC2231ECOMM.json", timeout=60)
r.raise_for_status()
d = r.json()

df = pd.DataFrame.from_dict(d["variables"], orient="index")
df.index.name = "variable"
df = df.reset_index()
df.to_csv(f"{OUT}/group_EC2231ECOMM.csv", index=False)
print("group_EC2231ECOMM.py finished")