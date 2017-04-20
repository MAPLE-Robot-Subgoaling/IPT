
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol1 = input("Please enter a symbol for the box outline: ")
    symbol2 = input("Please enter a symbol for the box fill: ")

    widthNew = width - 2
    symbolLine = (symbol1 * width)
    symbolList2 = (symbol2 * widthNew) 
    heightNew = height - 2

    print(symbolLine)

    for i in range(heightNew):
        print(symbol1 + symbolList2 + symbol1)    
    
    if height > 1:
        print(symbolLine)

main()
