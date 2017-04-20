
def main():
    widthNum = int(input("Please enter the width of box:"))
    heightNum = int(input("Please enter the height of box:"))
    symOtl = input("Please enter symbol for box outline:")
    symFl = input("Please enter symbol for box fill:")
    for rowNum in range(1, heightNum + 1):
        if rowNum == 1 or rowNum == heightNum:
            print(symOtl * widthNum)
        else:
            printLine = symOtl + symFl * (widthNum - 1)
            printLine = printLine[0:widthNum - 1] + symOtl
            print(printLine)
        
main()
