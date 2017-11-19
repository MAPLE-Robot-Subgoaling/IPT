def main():
    boxWidth = input("Please enter the width of the box: ")
    boxHeight = input("Please enter the height of the box: ")
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    drawBox(boxWidth, boxHeight, boxOutline, boxFill)
def drawBox(boxWidth, boxHeight, boxOutline, boxFill):
    boxWidth = int(boxWidth)
    boxHeight = int(boxHeight)
    for drawBox in range(int(boxHeight)):
        if drawBox != 0 and drawBox != (int(boxHeight) - 1): 
            print(boxOutline + ((boxWidth - 2) * boxFill) + boxOutline)
        if drawBox == 0:
            print(boxOutline * boxWidth)
        if drawBox == int(boxHeight) - 1:
            print(boxOutline * boxWidth)
main()
