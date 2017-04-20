
def main():

    hailstoneHeight = int( input("Please enter the starting height of the h\
ailstone:"))
    print("Hail is currently at height", hailstoneHeight)

    while hailstoneHeight != 1:

        if hailstoneHeight % 2 == 0:
            hailstoneHeight = hailstoneHeight // 2
            print("Hail is currently at height", hailstoneHeight)
        
        if hailstoneHeight % 2 == 1:
            hailstoneHeight = (hailstoneHeight * 3) + 1
            print("Hail is currently at height", hailstoneHeight)

    print("Hail stopped at height", hailstoneHeight)


main()

