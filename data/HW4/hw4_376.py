def main():
    hailstoneHeight = int(input("Please enter the starting height of the hailstone: "))
    STOP_HEIGHT = 1
    while hailstoneHeight != STOP_HEIGHT:
        if hailstoneHeight % 2 == 0:
            hailstoneHeight = hailstoneHeight // 2
        elif hailstoneHeight % 2 == 1:
            hailstoneHeight = (hailstoneHeight * 3)+1
        print("Hailstone is currently at height",hailstoneHeight)
    print("Hail stopped at height",hailstoneHeight)
main()
