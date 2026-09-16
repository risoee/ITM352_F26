first = input ("Enter the first name: ")
middle_initial = input ("Enter the middle initial: ")
last = input ("Enter the last name: ")

full_name = first + " " + middle_initial + "." + last
print("Your full name is:", full_name)

print (f"Your full name is: {first} {middle_initial}. {last}")
print("Your full name is: %s %s. %s" % (first, middle_initial, last))
print ("Your name using format method is: {0} {1}. {2}".format(first, middle_initial, last))
print ("Your name using list joins is: " + " ".join([first, middle_initial + ".", last]))