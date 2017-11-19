def main():
    hailHeight = int(input("Please enter the starting height of the hailstone: "))
    while hailHeight != 1:
        print("Hail is currently at height", hailHeight)
        if hailHeight % 2 == 0:
            hailHeight = int(hailHeight / 2)
        elif hailHeight % 2 == 1:
            hailHeight = int((hailHeight * 3) + 1)
    print("Hail is stopped at height 1")
main()
