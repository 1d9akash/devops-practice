def calculate_square(n):
    return n**2

try:
    user_input = int(input("Input: "))
    print("Output:", calculate_square(user_input))
except ValueError as e:
    print(f"Error: {e} | Please enter a valid Integer.")