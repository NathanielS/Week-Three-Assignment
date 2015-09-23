# Nathaniel Smith
# PigLatin
# Week Three Assignment
# This program will take input from the usar, translate it to PigLatin,
# and print the translated word.

def main ():
# This section of code ask for input from the usar and defines vowels
    word = input("Please enter an English word: ")
    vowels = "AEIOUaeiou"
    
# This section of code translates the usars input into PigLatin
    if word[0] in vowels:
        print(word + "yay")
    else:
        print(word[1:] + word[0] + "ay")
        
main ()