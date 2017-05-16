
def main():

    
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))

    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")

    outlineLine = outlineSymbol * boxWidth
    fillLine = outlineSymbol + fillSymbol * (boxWidth - 2) + outlineSymbol
    
    print(outlineLine)

    for i in range(boxHeight - 2):
        print(fillLine)

    print(outlineLine)

main()
