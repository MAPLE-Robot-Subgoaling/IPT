
def main():
    width = int(input("Please enter the width of the box: "))
    height= int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter the symbol for the box outline: ")
    symbolFill = input("Please enter the symbol for the box fill: ")
    if (height !=1 and width !=1):
        print(width * symbolOutline)
        width2 = width -2
        height2 = height-2
        for w in range (height2):
            print(symbolOutline + symbolFill *width2 +symbolOutline)
        print(width *symbolOutline)
    else:
        print(symbolOutline)

    

main()
