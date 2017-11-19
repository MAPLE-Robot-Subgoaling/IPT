def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter the symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    for i in range(height):
        if i == 0 or i == (height - 1):
            print(symbolOutline * width)
        else:
            print(symbolOutline + symbolFill * (width - 2) + symbolOutline)
main()
