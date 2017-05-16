
def main():
    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
    outSym = input("Enter a symbol for the box outline: ")
    fill = input("Enter a symbol for the box fill: ")

    tbLines = ""
    for i in range(width):
        tbLines = tbLines + outSym;
    
    fillLines = ""
    for i in range(width):
        if (i == 0 or  i == width - 1):
            fillLines = fillLines + outSym
        else:
            fillLines = fillLines + fill

    for i in range(height):
        if (i == 0 or i == height - 1):
            print(tbLines)
        else:
            print(fillLines)


main()
