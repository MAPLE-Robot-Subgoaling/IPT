def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    print(outlineSymbol * width)
    for i in range(1, height - 1):
        print(outlineSymbol + (fillSymbol * (width - 2)) + outlineSymbol)
    print(outlineSymbol * width)
main()
