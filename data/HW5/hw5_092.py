def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    widthList = list(range(0,width))
    heightList = list(range(0,height))
    if(height == 1 and width == 1):
        print(symbolOutline)
    else:
        print(symbolOutline * width)   
        for i in heightList:
            print(symbolOutline + (symbolFill * (width-2)) + symbolOutline)
        print(symbolOutline * width)
main()
