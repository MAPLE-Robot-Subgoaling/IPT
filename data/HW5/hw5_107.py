def main():
    print()
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    print()
    for i in range(0, height):
        if (i == 0) or (i == (height - 1)):
            print(symbolOutline * width)
        else:
            print(symbolOutline + (symbolFill * (width - 2)) + symbolOutline)
the proper number of fill symbols, encased in two outline symbols
    print()
main()
