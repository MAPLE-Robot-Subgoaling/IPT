def main():
    startingHeight = 0
    startingHeight = int(input("Please enter the starting height of the hailstone:"))
    while startingHeight != 1:
        if startingHeight % 2 == 0:
            print("Hail is currently at height ", startingHeight)
            startingHeight = startingHeight // 2
        elif startingHeight % 2 != 0:
            print("Hail is currently at height ", startingHeight)
            startingHeight = startingHeight * 3 + 1
    print("Hail stopped at height 1")
main()
