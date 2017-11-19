def main():
    width = int(input("Enter the width of the box: "))
    length = int(input("Enter the length of the box: "))
    outlineSym = input("Enter the symbol that will outline the box: ")
    fillSym = input("Enter the symbol that will fill the box: ")
    for i in range(length):
        if (i < (length - 1)) and (i > 0):
            print(outlineSym + (fillSym * (width - 2)) + outlineSym)
        else:
            print(outlineSym * width)
main()
