
def main():

    startHeight = int(input("Please enter the starting height of the hailstone: "))

    mod = startHeight % 2
    evnHeight = startHeight/2
    oddHeight = (startHeight * 3) + 1

    while startHeight != 1:
        print("Hail is currently at",startHeight)
        if mod == 0:
            startHeight = evnHeight
        if mod != 0:
            startHeight = oddHeight

    print("Hail stopped at height 1")
main()
