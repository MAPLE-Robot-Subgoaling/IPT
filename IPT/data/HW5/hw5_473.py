
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")

    if width <= 1 or height <= 1:
        if height > width:
            for a in range(height):
                a = outlineSymbol
                print(a)
        else:
            print(outlineSymbol * width)

    else:
        print(width * outlineSymbol)
        for b in range(height - 2):
            a = outlineSymbol
            b = fillSymbol
            formula = (a + (b * (width - 2)) + a)
            print(formula)
        print(width * outlineSymbol)

        
main()
