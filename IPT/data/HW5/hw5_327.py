
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOutline = str(input("Please enter a symbol for the box outline: "))
    symbolFill = str(input("Please enter a symbol for the box fill: "))

    for x in range(height):
        if(x == 0):
            print(symbolOutline * width)
        elif(x == height - 1):
            print(symbolOutline * width)
        else:
            print(symbolOutline + (symbolFill * (width - 2)) + symbolOutline)

main()
