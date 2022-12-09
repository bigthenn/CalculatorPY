# Define a function that takes two numbers and a mathematical operator as arguments
def calculate(num1, num2, operator):
  # If the operator is "+", return the sum of the numbers
  if operator == "+":
    return num1 + num2
  # If the operator is "-", return the difference of the numbers
  elif operator == "-":
    return num1 - num2
  # If the operator is "*", return the product of the numbers
  elif operator == "*":
    return num1 * num2
  # If the operator is "/", return the quotient of the numbers
  elif operator == "/":
    return num1 / num2

# Prompt the user for two numbers and a mathematical operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the mathematical operator (+, -, *, or /): ")

# Call the calculate function and print the result
result = calculate(num1, num2, operator)
print("The result is:", result)
