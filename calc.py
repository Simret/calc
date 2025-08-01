num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
sign = input("Enter the sign:")

if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2
elif sign == '*':
    result = num1 * num2
elif sign == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"

else:
    "Please enter a correct sign"
print("Result=", result)
