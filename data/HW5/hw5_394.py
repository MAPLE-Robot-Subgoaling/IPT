def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enmter a symbol for the box fill: ")
    heightList = range(0, height - 2)
    widthList = range(0, width)
    print(symbolOutline * width)
    for h in heightList:
        print(symbolOutline + symbolFill * (width - 2) + symbolOutline)
    if width != 1 and height != 1:
        print(symbolOutline * width)
main()
