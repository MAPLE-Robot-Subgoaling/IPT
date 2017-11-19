def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symOut = input("Please enter a symbol for the box outline: ")
    symFill = input("Please enter a symbol for the box fill: ")
    if(height == 0 or height == 1):
        print(symOut * width)
    if(height == 2):
        print(symOut * width)
        print(symOut * height)
    if(height > 2):
        print(symOut * width)
        for i in range(0, height - 2):
            print(symOut + (symFill * (width - 2)) + symOut)
        print(symOut * width)
main()
