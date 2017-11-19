def main():
    print("Hello and welcome to our hailstone program.")
    hailstoneHeight = int(input("Please enter the starting height of the hailstone: "))
    while hailstoneHeight > 1:
        print("Hail is currently at height:", hailstoneHeight)
        if hailstoneHeight % 2 == 0:
            hailstoneHeight = hailstoneHeight//2
        else:
            hailstoneHeight = hailstoneHeight * 3 + 1
    print("Hail stopped at height:", hailstoneHeight)
main()
