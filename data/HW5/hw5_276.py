def main():
    widthOfBox = int(input("Please enter the width of the box:"))
    heightOfBox=int(input("Please enter the height of the box:"))
    symbolForBoxOutline= str(input("Please enter a symbol for the box outline:"))
    symbolForBoxFill= str(input("Please enter a symbol for the box fill:"))
    print()
    for i in range(1,heightOfBox,1):
        if i==1:
            print(symbolForBoxOutline,symbolForBoxOutline * (widthOfBox-2),symbolForBoxOutline)
        elif  i< heightOfBox :
            print(symbolForBoxOutline, symbolForBoxFill*(widthOfBox-2), symbolForBoxOutline)
    print(symbolForBoxOutline,symbolForBoxOutline * (widthOfBox-2),symbolForBoxOutline)
    print()
main()
