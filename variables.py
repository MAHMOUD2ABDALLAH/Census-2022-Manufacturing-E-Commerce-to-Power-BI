import os, json, requests, pandas as pd

BASE = "https://api.census.gov/data/2022/ecnecomm"
OUT = "output"
os.makedirs(OUT, exist_ok=True)

def keep_all(pairs):
    out = {}
    for k, v in pairs:
        while k in out:
            k += "_dup"
        out[k] = v
    return out

def get(url):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return json.loads(r.content, object_pairs_hook=keep_all)

d = get(BASE + "/variables.json")

df = pd.DataFrame.from_dict(d["variables"], orient="index") \
       .drop(columns="values", errors="ignore")
df.index.name = "variable"
df = df.reset_index()
df.to_csv(f"{OUT}/variables.csv", index=False)

for name, info in d["variables"].items():
    if "values" in info:
        items = info["values"].get("item", {})
        vals = pd.DataFrame({
            "code":  [k.split("_dup")[0] for k in items],
            "label": list(items.values()),
        })
        vals.to_csv(f"{OUT}/values_{name}.csv", index=False)
print("variables.py finished")