# Ask the user to enter a decimal number. Calculate the square of that number and print it out.
# Name: Rin Isoe
# Date: Sept. 2, 2026

#Ask user to input a decimal number. 
input_value = input("Enter a floating point number: ")
float_value = float(input_value)
squared_value = float_value ** 2

#Display the original number and its square.
print("You entered:", float_value)
print("The square of the number you entered is:", squared_value)