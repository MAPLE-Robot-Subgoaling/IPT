

def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    
    outlinedSym = input("Please enter a symbol for the box outline: ")
    filledSym = input("Please enter a symbol for the box fill: ")

    print(outlinedSym*width)

    for i in range(0,(height-2)):
        print(outlinedSym + filledSym*(width - 2) + outlinedSym)
    
    if height != 1:
        print(outlinedSym*width)
    else:
        print()

main()
