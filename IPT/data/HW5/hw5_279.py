

def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSym = input("Please enter the symbol for the box outline: ")
    fillSym = input("Please enter the symbol for the box fill: ")

    print(outSym * width)
    for n in range(height-2):
        if width >= 2:
            print(outSym + fillSym*(width-2) +  outSym)
        else:
            print(outSym)

    if (height > 1):
        print(outSym * width)

main()
