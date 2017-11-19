def main():
    widthBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    upperRow = symbolOutline*widthBox
    filler = symbolFill * (widthBox-2)
    middleRow = symbolOutline + filler + symbolOutline
    print(upperRow)
    index = 0
    for index in range(0,heightBox-1):
        if (index+2)< heightBox:
            print(middleRow)
            index += 1
            if (index+2)== heightBox:
                print(upperRow)
        if heightBox == 2:
                print(upperRow)
main()
