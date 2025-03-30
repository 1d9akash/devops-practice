import json

user_input = input("Input: ")
result = json.loads(user_input)

for key, value in result.items():
    print(f"{key.capitalize()}: {value}")