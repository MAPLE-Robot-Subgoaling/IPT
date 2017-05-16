

def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symOutline = input("Please enter a symbol for the box outline: ")
    symFill = input("Please enter a symbol for the box fill: ")

    for i in range(height):
        if (i == 0) or (i == (height - 1)):
            print(symOutline * width)
        else:
            print(symOutline + (symFill * (width - 2)) + symOutline)

main()
