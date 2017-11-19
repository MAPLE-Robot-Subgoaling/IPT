def main():
    length=int(input("Please enter the length of the box: "))
    width=int(input("Please enter the width of the box: "))
    outlineSym=input("Please enter a symbol for the box outline: ")
    fillSym=input("Please enter a symbol for the box fill: ")
    for row in range(width):
        if row == 0 or row == width-1:
            print(outlineSym*length)
        else:
            print(outlineSym + fillSym*(length-2) + outlineSym)
main()
