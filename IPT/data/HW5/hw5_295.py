

def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    outBox = (boxWidth * outlineSymbol)
    
    print(outBox)

    for a in range(boxHeight - 2):
        print(outlineSymbol + (fillSymbol *(boxWidth - 2)) + outlineSymbol)  
    if boxHeight > 1:
        print(outBox)
    print()


main()
