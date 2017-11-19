def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol1 = input("Please enter a symbol for the box outline: ")
    symbol2 = input("Please enter a symbol for the box fill: ")
    listOne = [1]*(height-2)
    print(symbol1*width)
    for var1 in listOne:
        print(symbol1+((symbol2)*(width-2))+symbol1)
    print(symbol1*width)
main()    
