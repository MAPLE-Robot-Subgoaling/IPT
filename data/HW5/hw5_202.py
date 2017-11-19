def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symOut = input("Please enter the symbol for the box outline: ")
    symFill = input("Please enter the symbol for the box fill: ")
    topRow = symOut*width
    midRow = symOut + symFill*(width-2) + symOut
    for x in range(0, height):
        if x == 0 or x == height-1:
            print(topRow)
        else:
            print(midRow)
main()
