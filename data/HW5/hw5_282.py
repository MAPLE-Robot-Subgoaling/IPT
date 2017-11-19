def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSymbol = input("Please enter a symbol for the outline: ")
    fillSymbol = input("Please enter a symbol for the fill: ")
    print(outSymbol * width)
    for i in range(0, height - 2):
        print(outSymbol + (fillSymbol * (width - 2)) + outSymbol)
    print(outSymbol * width)
main()
