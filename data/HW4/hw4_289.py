def main():
    currentHeight = []
    heightOfHailStone = int(input("Please enter the starting height of the hailstone:"))
    currentHeight.append(heightOfHailStone)
    heightOfHailStone = 0
    while currentHeight[-1] != "1":
        newHeight = currentHeight[-1]
        if newHeight[-1] == "2" or newHeight[-1]== "4" or newHeight[-1] == "6" \
                or newHeight == "8":
            newHeightOfStone == (newHeight // 2)
            currentHeight.append(newHeightOfStone)
            print("The current height of the hailing stone is", newHeightOfStone)
        elif newHeight[-1] == "1" or newHeight[-1] == "3" or newHeight[-1]== "5" \
                or newHeight[-1] == "7" or newHeight == "9":
            newHeightOfStone == ((3 * newHeight) + 1)
            currentHeight.append(newHeightOfStone)
            print("The current height of the hailing stone is",newHeightOfStone)
        else:
            print("Hail stopped atheight 1")
main()
