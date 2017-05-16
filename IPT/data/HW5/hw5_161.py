


def main():
    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    symbolOutline = input("Please enter a symbol for the box outline:")
    symbolFill = input("Please enter a symbol for the box fill:")

    
    if width > 1 : 
        print(width * symbolOutline)
    for i in range(height-2):
        print(symbolOutline + symbolFill * (width - 2) + symbolOutline)
    print(width * symbolOutline)


main()
