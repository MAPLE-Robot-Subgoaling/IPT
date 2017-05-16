
def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the bow: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol fo the box fill: ")

    for lineNum in range(boxHeight):
        if lineNum == 0 or lineNum == boxHeight - 1:
            print(boxOutline * boxWidth)
        else:
            print(boxOutline + boxFill * (boxWidth - 2) + boxOutline)

main()
