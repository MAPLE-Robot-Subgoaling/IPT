def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    outSymbol = input("Please enter a symbol for the box outline: ")
    inSymbol = input("Please enter a symbol for the box fill: ")
    newWidth = range(boxWidth)
    newHeight = range(boxHeight)
    symbolOutside = outSymbol*boxWidth
    for i in newWidth:
        symbolInside = inSymbol *(boxWidth - 2)
    for i in newHeight:
            print(outSymbol+symbolInside+outSymbol)
main()
