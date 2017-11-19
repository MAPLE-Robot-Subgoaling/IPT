def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol1 = input("Please enter the symbol for the box outline: ")
    symbol2 = input("Please enter the symbol for the box fill: ")
    symHeight = height*symbol1
    for i in symHeight:
        print(symbol1*width) and print(i)
main()
