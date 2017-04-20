
def main():
    startHeight = int(input("Please enter the starting height of the hailstone: "))

    while startHeight != 1:
        curHeight = startHeight % 2
        while curHeight == 0:
            startHeight = startHeight // 2
        while curHeight == 1:
            startHeight = (startHieght*3)+1
        print("Hail is currently at height ", startHeight)

    print("Hail is stopped at height 1")


main()
