def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutlineSymbol = input("Please enter a symbol for the box outline: ")
    boxFillSymbol = input("Please enter a symbol for the box fill: ")
    boxOutlineString = ""
    boxFillString = boxOutlineSymbol
    for x in range(0, boxWidth):
        boxOutlineString = boxOutlineString + boxOutlineSymbol
    for z in range(0, boxWidth - 2):
        boxWidth > 1
        boxFillString = boxFillString + boxFillSymbol
    if boxWidth > 1:
        boxFillString = boxFillString + boxOutlineSymbol
    else:
        boxFillString = boxFillString
    if boxHeight > 2:
        print(boxOutlineString)
        for x in range(0, boxHeight - 2):
            print(boxFillString)
        print(boxOutlineString)
    else:
        for i in range(0, boxHeight):
            print(boxOutlineString)
main()
