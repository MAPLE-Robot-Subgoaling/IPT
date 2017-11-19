def main():
    hailHeight = int(input("Please enter the starting height of the hail: "))
    while hailHeight != 1:
        if hailHeight % 2 == 0:
            hailHeight = int(hailHeight / 2)
            print("The hail height is currently at", hailHeight)
        elif hailHeight % 2 != 0:
            hailHeight = hailHeight * 3 + 1
            print("The hail height is currently at", hailHeight)
    if hailHeight == 1:
        print("Hail stopped at height 1.")
main()
