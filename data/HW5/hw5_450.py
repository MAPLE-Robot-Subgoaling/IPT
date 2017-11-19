def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    for i in range (0, boxHeight):
        if i == 0 or i == (boxHeight - 1):
            print(outlineSymbol * boxWidth)
        else:
            outside = outlineSymbol
            inside = fillSymbol * (boxWidth - 2)
            print(outside + inside + outside)
main()
