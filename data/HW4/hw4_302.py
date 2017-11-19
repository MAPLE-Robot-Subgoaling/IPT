def main():
    hailHeight = int(input("Please enter the starting height of the hailstone: "))
    while hailHeight != 1:
        if hailHeight % 2 == 0:
            hailHeight = int(hailHeight/2)
            print("Hail is currently at height", hailHeight)
        else:
            hailHeight = int((hailHeight * 3) + 1)
            print("Hail is currently at height", hailHeight)
    print("Hail stopped at height 1")
main()
