def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSym = input("Please enter a symbol for the box outline: ")
    inSym = input("Please enter a symbol for the box fill: ")
    inSym = inSym * (width - 2)
    height = height + 1
    for x in range(height):
        if x == 0:
            print(outSym * width)
        elif x < height - 1:
            print(outSym + inSym + outSym)
        else:
            print(outSym * width)
main()
