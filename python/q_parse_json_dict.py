import json

try:
    user_input = input("Input: ")
    result = json.loads(user_input)
    if not isinstance(result, dict):
        raise ValueError("The Input must be a JSON object.")
    for key, value in result.items():
        print(f"{key.capitalize()}: {value}")
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON | {e}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")