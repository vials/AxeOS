import requests

response = requests.get('http://X.X.X.X/api/system/info') # Replace with your host/IP

json_data = response.json()
pools = []
for pool in json_data.get("pools"):
    pools.append(pool)

print(f"Using fallback server: {bool(json_data.get('isUsingFallbackStratum'))}")

primary_pool = json_data.get("pools")[json_data.get("primaryPoolIndex")]
secondary_pool = json_data.get("pools")[json_data.get("secondaryPoolIndex")]
print(f"Primary pool info: {primary_pool.get('stratumURL')}:{primary_pool.get('stratumPort')}")
print(f"Secondary pool info: {secondary_pool.get('stratumURL')}:{secondary_pool.get('stratumPort')}")
