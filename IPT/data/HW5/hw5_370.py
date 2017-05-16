
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOut = input("Please enter a symbol for the box outline: ")
    symbolIn = input("Please enter a symbol for the box fill: ")
    width2 = width - 2
    height2 = height - 2
    first = (symbolOut * width)
    middle = symbolOut+(symbolIn*width2)+symbolOut
    last = (symbolOut * width)
    myList = range(0,height2,1)
    
    print(first)
    for i in myList:
        print (middle)

    if height != 1:
        print(last)
        
main()
