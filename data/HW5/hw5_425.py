def main ():
    width = (int (input ("Please enter the width of the box: ")))
    height = (int (input ("Please enter the height of the box: ")))
    outline = (input ("Please enter a symbol for the box outline: "))
    fillSymbol = (input ("Please enter a symbol for the box fill: "))
    print (outline * width)
    for b in range (height - 2):
        print(outline + fillSymbol * (width - 2) + outline)
    print (outline * width)
main()
