def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    print ()
    print(symbolOutline * boxWidth)
    for row in range(boxHeight - 2):
        print(symbolOutline + symbolFill*(boxWidth - 2) + symbolOutline)
    print(symbolOutline * boxWidth)
    print ()
main()
