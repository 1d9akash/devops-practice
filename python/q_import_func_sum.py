try: 
    from math_operations import add

    user_input_a = float(input("Enter the Value for (a): "))
    user_input_b = float(input("Enter the Value for (b): "))

    print("Output: ",end="")
    print(add(user_input_a,user_input_b))

except ImportError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: Please Enter a Valid Number | {e}")
except Exception as e:
    print(f"Error: {e}")