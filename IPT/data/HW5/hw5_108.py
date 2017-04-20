
def main():

    width = int(input("Please choose a width: "))
    height = int(input("Please choose a height: "))
    widthSym = str(input("Please enter a symbol for the outline of the box: "))
    heightSym = str(input("Please enter a symbol for the box fill: "))
    
    if height == 1:
        print(widthSym)
    elif height == 0:
        print('')
    else:
        print(widthSym * width)
        for h in range(height - 2): 
            print(widthSym + ((width-2) * heightSym) + widthSym)
    
        print(widthSym * width)


main()
