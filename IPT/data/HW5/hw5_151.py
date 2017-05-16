
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symboloutside = input("Please enter a symbol for the box outline: ")
    symbolinside = input("Please enter a symbol for the box fill: ")
    insidewidth = width - 2
    fillingheight = height - 2
    print(symboloutside * width)
    for i in range(fillingheight):
        print(symboloutside + symbolinside * insidewidth + symboloutside)
    print(symboloutside * width)

main()
