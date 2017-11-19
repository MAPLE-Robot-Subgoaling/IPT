def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input(" Please enter the height of the box: "))
    symboOutline = input("Please enter a symbol for the box outline: ")
    symboFill = input("Please enter a symbol for the box fill: ")
    print(symboOutline * width)
    for x in range(height):
        print(symboOutline + symboFill * (width - 2) + symboOutline)
    print(symboOutline * width)
main()
