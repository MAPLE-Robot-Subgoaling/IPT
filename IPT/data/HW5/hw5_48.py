
def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")

    boxHeight = boxHeight - 1

    boxRange = range(0, (boxHeight + 1))

    topAndBottom = boxOutline * boxWidth
    middleOfBox = boxOutline + ((boxWidth - 2) * boxFill) + boxOutline

    for boxLine in boxRange:
        if boxLine == 0 or (boxLine == boxHeight and boxHeight != 1) or boxWidth == 1:
            print(topAndBottom)
        elif boxHeight != 1:
            print(middleOfBox)
main()
