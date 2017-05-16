
def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    outSymbol = str(input("Please enter a symbol for the box outline: "))
    fillSymbol = str(input("Please enter a symbol for the box fill: "))

    print(outSymbol*boxWidth)
    for i in range(boxHeight - 2):
        print(outSymbol + (fillSymbol * (boxWidth-2)) + outSymbol)
    if boxWidth > 1:
        print(outSymbol*boxWidth)

main()

