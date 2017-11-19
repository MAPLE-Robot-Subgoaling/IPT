def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    print (symbolOutline * boxWidth)
    for i in range(0,(boxHeight - 2)):
        print (symbolOutline + (symbolFill * (boxWidth - 2)) + symbolOutline)
    print (symbolOutline * boxWidth)        
main()
