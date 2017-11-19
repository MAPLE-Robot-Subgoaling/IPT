def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    fillWidth = boxWidth - 2
    fillHeight = boxHeight - 2
    print(symbolOutline*boxWidth)
    for n in range(fillHeight):
        print(symbolOutline + symbolFill*fillWidth + symbolOutline)
    if fillHeight > 0:
        print(symbolOutline*boxWidth)
main()
