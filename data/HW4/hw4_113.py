def main():
    currentHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", currentHeight)
    while (currentHeight != 1):
        if currentHeight % 2 == 0:
            currentHeight = currentHeight / 2
            print("Hail is currently at height", int(currentHeight))
        elif currentHeight % 2 != 0:
            currentHeight = currentHeight * 3 + 1
            print("Hail is currently at height", int(currentHeight))
    if (currentHeight == 1):
        print("Hail stopped at 1")
main()
