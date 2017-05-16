
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symb1 = input("Please enter a symbol for the box outline: ")
    symb2 = input("Please enter a symbol for the box fill: ")

    width1 = width - 2
    fill = symb2 *width1
    
    outer = symb1 * width
    print(symb1 * width)
    for a in range(0,height-1):
        
        print(symb1+fill+symb1)

    print(symb1 * width)

main()
