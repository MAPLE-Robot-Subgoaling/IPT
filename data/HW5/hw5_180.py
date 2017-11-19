def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter the symbol for the box outline: ")
    fillSymbol = input("Please enter the symbol for the box fill: ")
    for i in range(0, height, 1):
        if(i == 0 or i == (height-1)):
            print(outlineSymbol*width)
        else:
            print(outlineSymbol + fillSymbol * (width -2)+ outlineSymbol)
main()
