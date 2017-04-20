
def main():
    
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = str(input("Please enter a symbol for the box outline: "))
    boxFilling = str(input("Please enter a symbol for the box filling: "))

    print(boxOutline * boxWidth)

    for i in range(boxHeight - 2):
        if (boxWidth > 1):
            print(boxOutline + (boxFilling *(boxWidth -2)) + boxOutline)
        if (boxWidth == 1):
            print(boxOutline)
    if (boxHeight > 1):
        print(boxOutline * boxWidth)

main()
