
def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxHeight = int(input("Please enter the height of the box: "))
    boxFill = input("Please enter the a symbol for the box fill: ")
    for num in range(boxHeight):
        if num == 0 or num == (boxHeight-1):
            print(boxOutline * boxWidth)
        else:
            print(boxOutline + (boxFill*(boxWidth-2)) + boxOutline)

main()
