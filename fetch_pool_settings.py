import requests, json

response = requests.get('http://X.X.X.X/api/system/info') # Replace with your IP

json_data = response.json()

primary_pool_index = json_data.get("primaryPoolIndex")
secondary_pool_index = json_data.get('secondaryPoolIndex')


# Can be used to parse primary and fallback. Leftover code for the lazy people, but I am lazy too.
"""for pool in json_data.get("pools"):
    if pool.get("id") == primary_pool_index:
        print(f"Primary Pool Info:\n{pool}")
    elif pool.get("id") == secondary_pool_index:
        print(f"Secondary Pool Info:\n{pool}")
"""

generate_json = {
        "primaryPoolIndex":primary_pool_index,
        "secondaryPoolIndex":secondary_pool_index, #This is the payload needed to patch to your device if needed
        "pools":json_data.get("pools")
        }

print(json.dumps(generate_json))
