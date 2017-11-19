def main():
    startingHeight = abs(int(input("What is the current height of the hailstone?")))
    currentHeight = startingHeight
    print("Hailstone is currently at height", currentHeight)
    while currentHeight != 1:
        if currentHeight % 2 == 0:
            currentHeight = currentHeight / 2
            print("Hailstone is currently at height", currentHeight)
        elif currentHeight % 2 == 1:
            currentHeight = (currentHeight * 3) + 1
            print("Hailstone is currently at height", currentHeight)
    print("Hail stopped at height 1")
main()
