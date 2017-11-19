def main():
    startingHeight = int(input("Please enter the starting height of the hailstone: "))
    while startingHeight != 1:
        if startingHeight%2 == 0:
            startingHeight = startingHeight / 2
            print("The hail is currently at height", startingHeight)
        else:
            startingHeight = startingHeight * 3 + 1
            print("The hail is currently at height", startingHeight)
    else:
        print("Hail stopped at height 1")
main()
