
def main(): 
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    if height == 1:
        print(boxOutline * width)
    elif width == 1:
        for h in range(0, height + 1):
            print(boxOutline)
    else:
        print(boxOutline * width)
        for b in range(0, height - 2):
            print(boxOutline + (boxFill * (width - 2)) + boxOutline)
        print(boxOutline * width)

main()
