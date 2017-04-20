




def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = str(input("Please enter a symbol for the box outline: "))
    boxFill = str(input("Please enter a symbol for the box fill: "))

    yourBox = list(range(0, boxHeight - 2))
    
    print((boxOutline) * boxWidth)
    for boxInsides in yourBox:
        print(boxOutline + ((boxFill) * ((boxWidth - 2))) + boxOutline)
    if boxHeight > 1:
        print((boxOutline) * boxWidth)


main()
