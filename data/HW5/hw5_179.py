def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the outline: ")
    boxFill = input("Please enter a symbol for the fill: ")
    for i in range(1, height + 1, 1):
        if i == 1:
            print(boxOutline * width)
        elif (i > 1) and (i < height):
            print(boxOutline + (boxFill * (width - 2)) + boxOutline)
        else:
            print(boxOutline * width)
main()
