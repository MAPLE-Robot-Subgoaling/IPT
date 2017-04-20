
def main():

    ODD_CONSTANT = 1
    EVEN_DIVISOR = 2
    ODD_MULTIPLE = 3
    ADD_ONE = 1
    STOP_HAIL = 1

    hailHeight = int(input("Please enter a positive integer for the starting height of the hailstone: "))
    print("Hail is currently at height",hailHeight)
    while hailHeight != STOP_HAIL:
        if (hailHeight % EVEN_DIVISOR)== 0:
            hailHeight = hailHeight // EVEN_DIVISOR
            if hailHeight != STOP_HAIL:
                print("Hail is currently at height",hailHeight)
            elif hailHeight == STOP_HAIL:
                print("Hail stopped at height",hailHeight)
        elif (hailHeight % EVEN_DIVISOR == ODD_CONSTANT):
            hailHeight = (hailHeight * ODD_MULTIPLE)+ ADD_ONE
            if hailHeight != STOP_HAIL:
                print("Hail is currently at height",hailHeight)
            elif hailHeight == STOP_HAIL:
                print("Hail stopped at height",hailHeight)

main()
