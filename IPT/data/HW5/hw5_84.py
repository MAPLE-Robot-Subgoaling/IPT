

def main() :
    boxWidth = int(input("Enter the width of a box: "))
    boxHeight = int(input("Enter the height of a box: "))
    boxSymbolOutline = input("Enter a symbol to outline a box: ")
    boxSymbolFill = input("Enter a symbol to fill a box: ")
    for w in range(0, boxHeight):
        if  w >  0 and w != boxHeight - 1 :
            print(boxSymbolOutline + boxSymbolFill*(boxWidth - 2) + boxSymbolOutline)
        else :
            print(boxSymbolOutline * boxWidth)

main()
