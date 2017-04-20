def main():
    startingHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height: ", startingHeight)
    while startingHeight != 2:
        if startingHeight % 2 == 1:
            startingHeight = int((startingHeight * 3) + 1)
            print("Hail is currently at height: ", startingHeight)
        elif startingHeight % 2 == 0:
            startingHeight = int((startingHeight / 2))
            print("Hail is currently at height: ", startingHeight)
    print("Hail stopped at height: 1")


main()
