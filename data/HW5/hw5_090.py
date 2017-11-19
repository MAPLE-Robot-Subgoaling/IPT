def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOut = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    print(symbolOut * width)
    for i in range(height - 2):
        print(symbolOut + symbolFill * (width - 2) + symbolOut)
    if(height > 1):
        print(symbolOut * width)
main()
