def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    for i in range(1, boxHeight +1, 1) :
        if (i == 1) or (i == boxHeight):
             boxTop = boxOutline* boxWidth
             print (boxTop)
        else:
            boxInside = boxOutline + (boxFill *(boxWidth - 2)) + boxOutline
            print(boxInside)
        i = i + 1
main()
