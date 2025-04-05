try:
    pi = 3.14159
    r = float(input("Enter the radius: "))
    area = (pi)*(r)**2
    print("Output: ", area)
except ValueError:
    print("Error: Enter a Valid Number")
except Exception as e:
    print(f"Error: {e}")