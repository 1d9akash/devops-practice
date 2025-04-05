try:
    user_input = int(input("Input: "))
    if user_input % 4 == 0 and user_input % 100 !=0 or user_input % 400 == 0:
        print('Output: "Leap Year"')
    else:
        print('Output: "Not A Leap Year"')
except ValueError as e:
    print(f"Please Enter a Valid Year | {e}")
except Exception as e:
    print(f"Error: {e}")