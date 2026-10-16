# Name: Nathan Lenahan
# KUID: 3178995
# LAB Session (Day/Time): Wednesday 11am
# LAB Assignment: Lab 6
# Description: This program implements the Binomial Theorem of Section 6.4
#              to expand input expressions of the form (x+y)^n
# Collaborators/Sources: None

import sys
import math

def get_input(mode):
    """
    Reads the (x+y)^n expression from command line arguments if provided,
    otherwise prompts the user. Strips all whitespace.

    mode == 1: returns the full cleaned expression as a string, e.g. "(x+y)^4"
    mode == 0: returns only the exponent n as an int, e.g. 4
    """
    if len(sys.argv) > 1:
        raw = " ".join(sys.argv[1:])
    else:
        raw = input("Enter expression (e.g. (x+y)^4): ")

    # Remove all whitespace
    cleaned = "".join(raw.split())

    if mode == 0:
        # Keep only digit characters, then convert to int
        digits = "".join(ch for ch in cleaned if ch.isdigit())
        return int(digits)

    return cleaned

#Binomial Theorem Function
def binomial_theorem(n):

    #Loops through each term in the expansion
    for j in range(n+1):

        #Calculates binomial coefficient according to the formula from 6.4
        combination = math.factorial(n) // (math.factorial(j) * math.factorial(n - j))

        #Finds the x and y exponents for the current term
        x_exponent = n - j
        y_exponent = j

        #Goes through the exponents of x and y and prints each term
        #If an exponent is 0, the variable isn't printed
        #If an exponent is 1, the exponent isn't printed
        if y_exponent == 0:
            print (f"x^{x_exponent}", end="")
        elif x_exponent == 0:
            print (f"y^{y_exponent}", end="")
        elif x_exponent == 1 and y_exponent == 1:
            print (f"{combination}xy", end="")
        elif x_exponent == 1:
            print (f"{combination}xy^{y_exponent}", end="")
        elif y_exponent == 1:
            print (f"{combination}x^{x_exponent}y", end="")
        else:
            print (f"{combination}x^{x_exponent}y^{y_exponent}", end="")

        #Adds the plus sign between each term without adding one at the end
        if j < n:
            print(" + ", end="")

    #Prints new line after the expansion
    print()

if __name__ == "__main__":

    #Gets input and expands expression
    n = get_input(0)        
    binomial_theorem(n)