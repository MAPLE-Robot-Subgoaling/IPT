def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOut = str(input("Please enter a symbol for the box outline: "))
    symbolIn = str(input("Please enter a symbol for the box fill: "))
    for i in range(height):
        if i == 0 or i == height - 1:
            print(symbolOut * width)
        elif width == 1:
            print(symbolOut)
        else:
            print(symbolOut + symbolIn * (width - 2) + symbolOut)
main()
