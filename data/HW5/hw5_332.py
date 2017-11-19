def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOutline = input("Please enter the symbol for the box outline: ")
    symbolFill = input("Please enter the symbol for the box fill: ")
    for h in range(0, height):
        if h == 0 or h == height-1:
            for w in range(0, width):
                print(symbolOutline, end='')
            print()    
        else:
            for w in range(0, width):
                if w == 0 or w == width-1:
                    print(symbolOutline, end='')
                else:
                    print(symbolFill, end='')
            print()
main()
