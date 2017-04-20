
def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    
    for b in range(boxHeight):
        if b == 0 or b == boxHeight-1:
            print(boxOutline * boxWidth)
        else:
            print(boxOutline + boxFill * (boxWidth - 2) + boxOutline)
main()
