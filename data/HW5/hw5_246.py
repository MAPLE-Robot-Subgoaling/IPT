def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    for index in range(height):
        if(index == 0) or (index == (height-1)):
            print(symbolOutline * width)
        else:
            print(symbolOutline + (symbolFill * (width - 2)) + symbolOutline)
main()
