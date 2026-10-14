# Name: Nathan Lenahan
# KUID: 3178995
# LAB Session (Day/Time): Wednesday 11am
# LAB Assignment: Lab 6
# Description:
#
#
#
# Collaborators/Sources:
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

def binomial_theorem(n):

    for j in range(n+1):
        combination = math.factorial(n) // (math.factorial(j) * math.factorial(n - j))
        x_exponent = n - j
        y_exponent = j

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

        if j < n:
            print(" + ", end="")

    print()

if __name__ == "__main__":
    n = get_input(0)        
    binomial_theorem(n)