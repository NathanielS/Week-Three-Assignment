# Nathaniel Smith
# StarWars
# Week Three Assignment
# This program takes input from the usar in order to produce the usar's Star Wars name.

def main ():
    # This code take input from the usar.
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    maiden = input("Please enter your mother's maiden name: ")
    city = input("Please enter the city you were born in: ")
    
    # This code uses the usar's input to output their StarWars name
    print("Your Star Wars name is", lastName[0:3] + firstName[0:2], maiden[0:2] + city[0:3])
    
main ()