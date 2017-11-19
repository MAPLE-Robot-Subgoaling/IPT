def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symOut = input("Please enter a symbol for the box outline: ")
    symIn = input("Please enter a symbol for the box fill: ")
    print(symOut*width)
    if width >1:
        for i in range(height-1):
            print(symOut + symIn*(width-2) + symOut)
        print(symOut*width)
main()
