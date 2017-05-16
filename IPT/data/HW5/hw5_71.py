
def main(): 
    boxWidth = int(input("Please enter the width of the box: "))
    boxLength = int(input("Please enter the length of the box: "))
    boxOutline = str(input("Please enter a symbol for the box outline: "))
    boxFill = str(input("Please enter a symbol for the box fill: "))
    topAndBottomLine = (boxOutline * boxWidth)
    print(topAndBottomLine)
    for i in range(0, boxLength - 2):
        print(boxOutline + (boxFill * (boxWidth - 2)) + boxOutline)

    print(topAndBottomLine)

main()
    
