
def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = str(input("Please enter a symbol for the box outline: "))
    boxFill = str(input("Please enter a symbol for the box fill: "))
    
    fillLength = boxWidth - 2
    middleRows = boxOutline + (boxFill*fillLength)  + boxOutline

    print(boxOutline*boxWidth)
    for i in range(boxHeight-2):
        print(middleRows)
    print(boxOutline*boxWidth)

main()
