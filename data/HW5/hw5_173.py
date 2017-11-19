def drawBox(width, height, outline, fill):
    print()
    print(outline * width)
    for i in range(height - 2):
        print(outline + fill * (width - 2) + outline)
    print(outline * width)
    print()
def main():
    print("Welcome to the 133T ASCII Art Box program! ")
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    drawBox(boxWidth, boxHeight, outlineSymbol, fillSymbol)
    print("We flipped it...for funsies. Your height is your width,  your fill is your outline and vice versa! Enjoy.")
    drawBox(boxHeight, boxWidth, fillSymbol, outlineSymbol)
main()
