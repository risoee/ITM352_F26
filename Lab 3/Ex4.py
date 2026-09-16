
# Apply whichever temperature conversion function the caller supplies.
def convert_temperature(value, conversion_function):
	return conversion_function(value)


# Convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
	return (celsius * 9 / 5) + 32


# Convert Fahrenheit to Celsius.
def fahrenheit_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9


# Convert Celsius to Kelvin.
def celsius_to_kelvin(celsius):
	return celsius + 273.15


# Convert Kelvin to Celsius.
def kelvin_to_celsius(kelvin):
	return kelvin - 273.15


# Convert Fahrenheit to Kelvin.
def fahrenheit_to_kelvin(fahrenheit):
	return (fahrenheit - 32) * 5 / 9 + 273.15


# Convert Kelvin to Fahrenheit.
def kelvin_to_fahrenheit(kelvin):
	return (kelvin - 273.15) * 9 / 5 + 32


# Demonstrate callbacks using one temperature in each scale.
temperature = float(input("Enter a temperature in Celsius: "))
print(f"{temperature} Celsius is {convert_temperature(temperature, celsius_to_fahrenheit)} Fahrenheit")
print(f"{temperature} Celsius is {convert_temperature(temperature, celsius_to_kelvin)} Kelvin")
