def main():
    NO_FILL = 0
    FIRST_LINE = 1
    SEC_LINE = 2
    widBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    symOut = input("Please enter a symbol for the box outline: ")
    symFill = input("Please enter a symbol for the box fill: ")
    fillLine = widBox - SEC_LINE
    if fillLine >= NO_FILL  or  heightBox > FIRST_LINE:
        for p in range(FIRST_LINE):
            print(symOut * widBox)
        for p in range(SEC_LINE, heightBox):
            if widBox == FIRST_LINE:
                print (symOut)
            else:
                print(symOut + (symFill * fillLine) + symOut)
        for p in range(heightBox, heightBox + FIRST_LINE):
            print(symOut * widBox)
    else:
        print(symOut)
main()
