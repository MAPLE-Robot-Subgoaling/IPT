
def main():
    EVEN_DIV = 2
    ODD_MULT = 3
    ODD_SUPP = 1
    start = int(input("Enter the starting height of the hailstone: "))
    while (start <= 0):
        start = int(input("The height must be at least 1, try again: "))
    while (start > 1):
        print("Hail is currently at height:", start)
        if (start % 2 == 1):
            start = start * ODD_MULT + ODD_SUPP
        else:
            start = start // EVEN_DIV
    
    print("Hail stopped at height 1.")
main()
