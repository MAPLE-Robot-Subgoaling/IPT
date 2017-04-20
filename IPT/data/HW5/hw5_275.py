
def main():
    widthNum = int(input("Please enter the width of the box: "))
    heightNum = int(input("Please enter the height of the box: "))
    symbolOut = str(input("Please enter a symbol for the box outline: "))
    symbolFill = str(input("Please enter a symbol for the box fill: "))
    print(symbolOut * widthNum)
    for i in range(heightNum - 2) :
        print(symbolOut + (widthNum - 2) * symbolFill + symbolOut)
    print(symbolOut * widthNum)
main()
