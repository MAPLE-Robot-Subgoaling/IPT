def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    if (height == 1):
        print(outlineSymbol * width)
    elif (height == 2):
        print (outlineSymbol * width)
        print (outlineSymbol * width)
    else:
        print (outlineSymbol * width)
        for i in range(0, height - 2):
            print(outlineSymbol + fillSymbol * (width-2) + outlineSymbol)
        print(outlineSymbol * width)
main()
