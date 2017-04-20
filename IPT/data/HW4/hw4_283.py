


def main():
    startHeight = (input("please enter the starting height of the hailstones: "))
    while startHeight != "1":
        if startHeight[-1] == "0" or startHeight[-1] == "2" or startHeight[-1] == "4" or startHeight[-1] == "6" or startHeight[-1] == "8":
            startHeight = int(startHeight)
            startHeight = startHeight / 2
            print("Hail is currently at height ", (startHeight))
            startHeight = str(startHeight)
        elif startHeight[-1] == "1" or startHeight[-1] == "3" or startHeight[-1] == "5" or startHeight[-1] == "7" or startHeight[-1] == "9":
            startHeight = int(startHeight)
            startHeight = ((startHeight) * 3) + 1
            print("Hail is currently at height ", (startHeight))
            startHeight = str(startHeight)
    print("Hail stopped at height 1. ")

      
main()
