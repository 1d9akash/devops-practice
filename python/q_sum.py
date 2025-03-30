user_input=input("Input: ").split(",")
int_input= []
for num in user_input:
    int_input.append(int(num))
print("Sum =",sum(int_input))