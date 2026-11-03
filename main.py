import os, json, requests, pandas as pd
from census_key import get_key

BASE = "https://api.census.gov/data/2022/ecnecomm"
OUT = "output"
os.makedirs(OUT, exist_ok=True)
KEY = get_key()

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

def save(df, name):
    df.to_csv(f"{OUT}/{name}.csv", index=False)

save(pd.DataFrame(get(BASE + "/geography.json")["fips"]), "geography")

d = get(BASE + "/variables.json")
df = pd.DataFrame.from_dict(d["variables"], orient="index").drop(columns="values", errors="ignore")
df.index.name = "variable"
save(df.reset_index(), "variables")

for name, info in d["variables"].items():
    if "values" in info:
        items = info["values"].get("item", {})
        vals = pd.DataFrame({"code": [k.split("_dup")[0] for k in items], "label": list(items.values())})
        save(vals, f"values_{name}")

save(pd.DataFrame(get(BASE + "/groups.json")["groups"]), "groups")
d = get(BASE + "/groups/EC2231ECOMM.json")
g = pd.DataFrame.from_dict(d["variables"], orient="index")
g.index.name = "variable"
save(g.reset_index(), "group_EC2231ECOMM")

d = get(BASE + "/examples.json")
save(pd.DataFrame({"get": d.get("get", [])}), "examples_get")
save(pd.DataFrame(list(d.get("predicates", {}).items()), columns=["variable", "value"]), "examples_predicates")
save(pd.DataFrame(d.get("fips", [])), "examples_fips")

for name in ["tags", "sorts"]:
    d = get(f"{BASE}/{name}.json")
    save(pd.DataFrame(d.get(name, [])), name)

r = requests.get(f"{BASE}?get=group(EC2231ECOMM)&for=us:*&key={KEY}", timeout=60)
r.raise_for_status()
d = r.json()
save(pd.DataFrame(d[1:], columns=d[0]), "data")
print("main.py finished")
