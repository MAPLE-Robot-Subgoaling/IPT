def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOut = input("Please enter the symbol for the box outline: ")
    symbolIn = input("Please enter a symbol for the box fill: ")
    width2 = (width - 2)
    symbol1 = (width * symbolOut)
    
    print(symbol1)

    for i in range(1, height):
        print(symbolOut + symbolIn * width2 + symbolOut)
 
    print(symbol1)

    
main()
