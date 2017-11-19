def main():
    END_HEIGHT = 1
    startingHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", startingHeight)
    while startingHeight != 1:
        if startingHeight % 2 == 0:
            startingHeight = startingHeight // 2
            print("Hail is currently at height", startingHeight)
        elif startingHeight % 2 == 1:
            startingHeight =(startingHeight * 3) + 1
            print("Hail is currently at height", startingHeight)
    if startingHeight == 1:
        print("Hail stopped at height 1")
main()
