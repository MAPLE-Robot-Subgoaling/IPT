def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOut =  input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    printTemp = ""
    for h in range(height):
        if h == 0 or h == height-1:
            for w in range(width):
                printTemp = printTemp + symbolOut
            print(printTemp)
            printTemp = ""
        else:
            for w in range(width):
                if w == 0 or w == width-1:
                    printTemp = printTemp + symbolOut
                else:
                    printTemp = printTemp + symbolFill
            print(printTemp)
            printTemp = ""
main()
