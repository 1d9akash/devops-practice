import json
import os
try:
    if os.path.exists("user_details.json"):
        with open("user_details.json","r") as file:
            result = json.load(file)
            name = result.get('name', '<Not Found>')
            email = result.get('email', '<Not Found>')
            print(f"name: {name}")
            print(f"email: {email}")
    else:
        raise FileNotFoundError("Check whether the file 'user_details.json' is present or not.")
except Exception as e:
    print(f"Error: {e}")