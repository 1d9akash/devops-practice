try:
    user_input = int(input("Input: "))
    print("Output:")
    for i in range(1,11):
        print(f"{user_input} x {i} = {user_input*i}")
except ValueError as e:
    print(f"Error: Please Enter a Valid Integer | {e}")
except Exception as e:
    print(f"Error: {e}")