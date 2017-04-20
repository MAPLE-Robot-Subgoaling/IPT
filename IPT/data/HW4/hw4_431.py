''' File: hw4_part3.py 
    Author: Skye Ortiz 
    Date: 10/05/2016 
    Section: 26 
    E-mail: sortiz1@umbc.edu 
    Description: This program simulates the movement of a hailstone in a storm.
    Collaboration: Collaboration is not permitted on this assignment.
'''
def main():
    height = int(input("Please enter an integer starting height for the stone."))
    print("The hail started at height " + str(height))
    while height != 1:
        if height % 2 == 0:
            height = height // 2
            print("The current height of the hail is " + str(height))
        elif height % 2 == 1:
            height = height * 3 + 1
            print("The current height of the hail is " + str(height))
    print("The hail stopped at height 1.")
main()
