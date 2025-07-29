#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.


a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero is not allowed."


def print_result(a, b, operation, result):
    print(f"{a} {operation} {b} = {result}")
