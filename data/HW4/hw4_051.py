def main():
    hailstoneHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", hailstoneHeight)
    while hailstoneHeight != 1:
        if hailstoneHeight % 2 == 0:
            hailstoneHeight = hailstoneHeight / 2
            hailstoneHeight = int(hailstoneHeight)
            print("Hail is currently at height", hailstoneHeight)
        elif hailstoneHeight % 2 == 1:
            hailstoneHeight = hailstoneHeight * 3 + 1
            hailstoneHeight = int(hailstoneHeight)
            print("Hail is currently at height", hailstoneHeight)
main()
