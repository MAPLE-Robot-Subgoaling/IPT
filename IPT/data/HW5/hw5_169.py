
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSym = input("Please enter a symbol for the box outline: ")
    fillSym = input("Please enter a symbol to fill the box: ")
    if height == 1:
        print(outSym * width)
    elif height == 2: 
        print(outSym * width)
        print(outSym * width)
    else:
        print(outSym * width)
        for i in range (height - 2):
            print((outSym)+(fillSym * (width - 2))+(outSym))
        print(outSym * width)
main()
