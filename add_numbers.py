# Simple Python program to add two numbers

def add_numbers(num1, num2):
    return num1 + num2

# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Add the numbers
result = add_numbers(num1, num2)

# Display the result
print("The sum of", num1, "and", num2, "is:", result)
