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

df = pd.DataFrame(get(BASE + "/geography.json")["fips"])
df.to_csv(f"{OUT}/geography.csv", index=False)
print(df.to_csv(index=False))