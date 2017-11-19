def main():
    NO_BOX = 1
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height  of the box: "))
    symbolOutline = input("Please enter the symbol for the box outline: ")
    symbolFill =  input("Please enter the symbol for the box fill: ")
    if height == NO_BOX:
       print(symbolOutline*width)    
    else:
        print(symbolOutline*width)    
        for i in range(0,height - 2):
            print(symbolOutline + (symbolFill*(width-2)) + symbolOutline)
        print(symbolOutline*width)    
main()
