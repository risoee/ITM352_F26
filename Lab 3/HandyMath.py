# A collection of reusable math functions.


# Return the number halfway between two numbers.
def midpoint(number1, number2):
    return (number1 + number2) / 2


# Return the square root of a number.
def square_root(number):
    return number ** 0.5


# Raise the base to the given power.
def exponent(base, power):
    return base ** power


# Return the larger of two numbers.
def max(number1, number2):
    return number1 if number1 > number2 else number2


# Return the smaller of two numbers.
def min(number1, number2):
    return number1 if number1 < number2 else number2
