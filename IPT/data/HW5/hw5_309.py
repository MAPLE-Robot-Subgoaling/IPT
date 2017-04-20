
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    MARGIN = 2
    ONE_LESS_THAN_HEIGHT = height - 1
    for num in range(height):
        if (num == 0):
            print(symbolOutline * width)
        elif (num < ONE_LESS_THAN_HEIGHT):
            print(symbolOutline + symbolFill * (width - MARGIN) +  symbolOutline)
        else:
            print(symbolOutline * width)


main()
