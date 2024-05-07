# Assigning a string value to the variable myString
myString = "This is a string."
# Printing the value of myString
print(myString)

# Printing the data type of myString
print(type(myString))

# Concatenating strings to create a new string and printing the result along with its data type
print(myString + " is of the data type " + str(type(myString)))

# Assigning string values to two variables and concatenating them to create a third string
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
# Printing the concatenated string
print(thirdString)

# Asking the user to input their name
name = input("What is your name? ")
# Printing the name entered by the user
print(name)

# Asking the user to input their favorite color and favorite animal
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

# Printing a message using the user's name, favorite color, and favorite animal
print("{}, you like a {} {}!".format(name,color,animal))
