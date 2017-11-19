def main():    
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    insideBox = [boxOutline]*(boxHeight - 2)
    if boxWidth == 1 and boxHeight == 1:
        print(boxOutline)
    elif boxWidth == 2 and boxHeight == 1:
        print(boxOutline*2)
    elif boxWidth == 1 and boxHeight == 2:
        print(boxOutline)
        print(boxOutline)
    else:
        print(boxOutline * boxWidth)
        for symbol in insideBox:
            print(symbol + (boxFill * (boxWidth - 2)) + symbol)
        print(boxOutline * boxWidth)
main()
