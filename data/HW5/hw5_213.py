def main():
    boxWidth  = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    innerSymbol = input("Please emter a symbol for the box fill: ")
    innerRows = list(range(0 , boxHeight-2))
    print(outlineSymbol * boxWidth)
    for numOf  in innerRows:
       print(outlineSymbol + (innerSymbol*(boxWidth -2)) + outlineSymbol)
    if boxHeight > 1:
        print(outlineSymbol * boxWidth)
main()
