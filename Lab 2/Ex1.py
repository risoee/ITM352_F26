# This program prompts the user to enter a number between 1 and 100, converts the input to an integer, calculates the square of that number, and then prints both the original number and its square.   
# number, and then prints both the entred number and its sqaure. 
# Name: Rin Isoe 
# Date: Sept. 2, 2026
value_entered = input("Enter a number between 1 and 100:")
value_as_integer = int(value_entered)

valueSquared = value_as_integer ** 2

print("You entered:", value_as_integer)
print("The square of the number you entered is:", valueSquared)

print(f"You entered: {value_as_integer}, and the square of {value_as_integer} is: {valueSquared}")