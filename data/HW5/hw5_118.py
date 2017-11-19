def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter the symbol for the box outline: ")
    boxFill = input("Please enter the symbol for the box fill: ")
    for num1 in range(boxHeight):
        if num1 == 0 or num1 == boxWidth-1:
            print(boxOutline * boxWidth)
        else:
            print(boxOutline + boxFill * (boxWidth-1) + boxOutline)
main()
