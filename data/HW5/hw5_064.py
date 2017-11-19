def main():
    print ("This program will create a box.")
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    outlineSym = str(input("Please enter the symbol for the box outline: "))
    fillSym = str(input("Please enter the symbol for the box fill: "))
    for h in range(boxHeight):
        if h == 0 or h == (boxHeight -1):
            print(boxWidth * outlineSym)
        else:
            print(outlineSym + (fillSym * (boxWidth - 2)) + outlineSym)
main()
