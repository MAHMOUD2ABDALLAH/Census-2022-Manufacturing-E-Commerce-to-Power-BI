import os, requests, pandas as pd
from census_key import get_key

KEY = get_key()
URL = f"https://api.census.gov/data/2022/ecnecomm?get=group(EC2231ECOMM)&for=us:*&key={KEY}"

r = requests.get(URL, timeout=60)
r.raise_for_status()
d = r.json()
df = pd.DataFrame(d[1:], columns=d[0])

os.makedirs("output", exist_ok=True)
df.to_csv("output/data.csv", index=False)
print("data.py finished")