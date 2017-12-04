from dear_api import DEARSystemsAPI
import json

account = "58c6b4fb-6298-4b8d-9184-75697de6c956"
myKey = "e69e1668-4e51-ec89-0c40-20d4d90c3c62"

my_api = DEARSystemsAPI(account, myKey)

response = my_api.customers(include_deprecated=True, limit=1)
print(json.dumps(response, indent=4))

