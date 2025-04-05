try:
    user_input = input("Input (enter exactly 2 numbers, separated by a comma): ").split(",")
    if len(user_input) != 2:
        raise ValueError("You must enter exactly 2 numbers separated by a comma.")
    int_input= []
    for num in user_input:
        int_input.append(int(num.strip()))
    print("Sum =",sum(int_input))
except ValueError as e:
    print(f"Error: {e}")