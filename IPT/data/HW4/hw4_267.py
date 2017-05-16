
def main():
    startHeight = int(input("Please enter the starting height of the hailstone: "))
    currentHeight = startHeight
    while (currentHeight != 1):
        print("Hail is currently at height", currentHeight)
        if (currentHeight % 2 == 0):
            currentHeight = currentHeight // 2
        else:
            currentHeight = (currentHeight * 3) + 1
    print("Hail stopped at height 1")
main()
