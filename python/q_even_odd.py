try:
    user_input=int(input("Input: "))
    result = user_input % 2
    if result == 0:
        print('Output: "Even"')
    else:
        print('Output: "Odd"')
except ValueError as e:
    print(f"Error: Please Enter a Valid Integer | {e}")
except Exception as e:
    print(f"Error: {e}")