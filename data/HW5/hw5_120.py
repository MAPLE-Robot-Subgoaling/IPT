def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolO = input("Please enter a symbol for the box outline: ")
    symbolF = input("Please enter a symbol for the box fill: ")
    print(symbolO*width)
    for n in range(height-2):
        print(symbolO+symbolF*(width-2)+symbolO)
    if width != 1:
        print(symbolO*width)
main()
