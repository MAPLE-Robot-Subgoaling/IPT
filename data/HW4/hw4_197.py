def main():
    DIVIDE = 2
    MULT   = 3
    ADD    = 1
    hail   = int(input("Please enter the starting height of the hailstone: "))
    while hail > 1:
        if (hail % 2) == 0:
            print("Hail is currently at height", hail)
            hail = int(hail / DIVIDE)
        elif (hail % 2) == 1:
            print("Hail is currently at height", hail)
            hail = int((hail * MULT) + ADD)
    print("Hail stopped at height", hail)
main()
