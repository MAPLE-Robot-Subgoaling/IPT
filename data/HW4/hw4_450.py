def main():
    stoneHeight = int(input("Please enter the starting height of the hailstone: "))
    while stoneHeight > 1:
        print("The hailstone is currently at height",stoneHeight)
        if (stoneHeight % 2 == 0):
            stoneHeight = stoneHeight // 2
        else:
            stoneHeight = (stoneHeight * 3) + 1
    print("The hailstone stopped at height",stoneHeight)
main()
