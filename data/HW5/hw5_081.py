def main():
    widthOfBox=int(input("Please enter the width of the box: "))
    heightOfBox=int(input("Please enter the height of the box: "))
    symbolOut=input("Please enter a symbol for the box outline: ")
    symbolFill=input("Please enter a symbol for the box fill: ")
    for i in range (0,heightOfBox):
        if i==0 or i==heightOfBox-1:
            print(symbolOut*widthOfBox)
        else:
            print(symbolOut+(symbolFill*(widthOfBox-2))+symbolOut)
main()
