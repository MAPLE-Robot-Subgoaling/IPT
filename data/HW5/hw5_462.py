def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    print (boxOutline * width)
    for i in range (0, height - 2):
        print(boxOutline + boxFill * (width-2) + boxOutline)
    if (height > 1):
        print(boxOutline * width)
main()
