def main ():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOut = str(input("Please enter a symbol for the box outline: "))
    symbolFill = str(input("Please enter a symbol for the box fill: "))
    for i in range(height):
        if (i==0) or (i== height-1):
            print(width*symbolOut)
        else:
            print(symbolOut+symbolFill*(width-2)+symbolOut)
main()
