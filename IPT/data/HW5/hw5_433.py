
def main():
    widthBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    outSym = input("Please enter a symbol for the box outline: ")
    fillSym = input("Please enter a symbol for the box fill: ")
    for n in range(heightBox):
        if (n == 0 or n == (heightBox-1)):
            print(outSym*widthBox)
        else:
            print(outSym + (fillSym*(widthBox-2)) + outSym)

main()
