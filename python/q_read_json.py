import json

with open("user_details.json","r") as file:
    result = json.load(file)
print(f"name: {result['name']}")
print(f"email: {result['email']}")