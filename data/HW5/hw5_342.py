def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    drawOutline = width * outlineSymbol
    drawFill = ""
    for i in range(height):
        if i == 0 or i == height-1:
            print(drawOutline)
        else:
            drawFill = outlineSymbol + ((width-2)*fillSymbol) + outlineSymbol
            print(drawFill)
main()
