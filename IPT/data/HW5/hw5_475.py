

def main():

    width = int(input("What is the width of the box?"))
    height = int(input("What is the height of the box?"))
    outlineSymbol = str(input("What is the outline for the box?"))
    fillSymbol = str(input("What is the fill for the box?"))
    
    smallHeight = height - 2
    smallWidth = width - 2

    print(outlineSymbol * width)
    for i in range(smallHeight):
        print(outlineSymbol + fillSymbol * smallWidth + outlineSymbol)
    print(outlineSymbol * width)



main()
