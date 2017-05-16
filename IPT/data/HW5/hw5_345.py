
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSym = input("Please enter a symbol for the box outline: ")
    inSym = input("Please enter a symbol for the box fill: ")
    for i in range(height):
        print (width * outSym)

main()
