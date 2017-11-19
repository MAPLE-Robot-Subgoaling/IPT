def main():
    width = int(input('Please enter the width of the box: '))
    height = int(input('Please enter the height of the box: '))
    symOutline = input('Please enter a symbol for the box outline: ')
    symFill = input('Please enter a symbol for the box fill: ')
    for hi in range(height):
        output = ''
        if hi == 0 or hi == height - 1:
            output = symOutline * width
        else:
            output = symOutline + symFill * (width - 2) + symOutline
        print(output)
main()
