import os, requests, pandas as pd

BASE = "https://api.census.gov/data/2022/ecnecomm"
OUT = "output"
os.makedirs(OUT, exist_ok=True)

r = requests.get(BASE + "/examples.json", timeout=60)
r.raise_for_status()
d = r.json()

pd.DataFrame({"get": d.get("get", [])}).to_csv(f"{OUT}/examples_get.csv", index=False)
pd.DataFrame(list(d.get("predicates", {}).items()), columns=["variable", "value"]).to_csv(f"{OUT}/examples_predicates.csv", index=False)
pd.DataFrame(d.get("fips", [])).to_csv(f"{OUT}/examples_fips.csv", index=False)
print("examples.py finished")