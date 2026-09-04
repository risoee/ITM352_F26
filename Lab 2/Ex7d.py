# This program will ask the user to enter a temperature in Fahrenheit and then convert it to Celsius and print out the result.
# Create the conversion as a function. 
# Name: Rin Isoe
# Date: Sept. 4, 2026

def F_to_C(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    rounded_celsius = round(celsius, 2)
    return rounded_celsius


fahrenheit_input = input("Enter a temperature in Fahrenheit: ")
fahrenheit_float = float(fahrenheit_input)

celsius_value = F_to_C(fahrenheit_float)

print("You entered:", fahrenheit_float)
print("The temperature in Celsius is:", celsius_value)