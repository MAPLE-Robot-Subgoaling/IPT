def main():
    currentHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", currentHeight) 
    while  currentHeight > 1:
        if currentHeight % 2 == 0:
            half = currentHeight // 2
            currentHeight = currentHeight - half
            currentHeight = int(currentHeight)
            print("Hail is currently at height", currentHeight)
        elif currentHeight % 3 == 0 and (currentHeight % 2) != 0:
            currentHeight = (3 * currentHeight) + 1
            currenttHeight = int(currentHeight)
            print("Hail is currently at height", currentHeight)
        else:
            currentHeight = (3 * currentHeight) + 1
            currentHeight = int(currentHeight)
            print("Hail is currently at height", currentHeight)
    if currentHeight == 1:
        print("Hail stopped at height 1")
main()
