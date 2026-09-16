import HandyMath
from HandyMath import max, min


# Get two numbers from the user for the math calculations.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))


# Use the functions from HandyMath and format the results with f-strings.
print(f"The midpoint is {HandyMath.midpoint(number1, number2)}")
print(f"The square root of the square of {number1} is {HandyMath.square_root(number1 ** 2)}")
print(f"{number1} raised to the exponent {number2} is {HandyMath.exponent(number1, number2)}")
print(f"The maximum is {max(number1, number2)}")
print(f"The minimum is {min(number1, number2)}")

# Pass functions as arguments and display each function's name and result.
print(HandyMath.describe_function(number1, number2, min))
print(HandyMath.describe_function(number1, number2, max))
print(HandyMath.describe_function(number1, number2, HandyMath.exponent))
