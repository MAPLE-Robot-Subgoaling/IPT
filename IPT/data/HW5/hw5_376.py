
def main():

    widthBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    width = widthBox - 2
    
    for i in range(0, heightBox , 1):
        if i == 0 or i == heightBox-1:
            print(boxOutline * widthBox)
        else:
            line = (boxFill * width)
            print(boxOutline + line + boxOutline)

main()
