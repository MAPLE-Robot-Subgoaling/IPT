
def main():
    
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSymbol = input("Please enter a symbol for the box outline: ")
    inSymbol = input("Please enter a symbol for the box fill: ")

    print(outSymbol * width)
    
    for h in range(0, height - 2):
        print(outSymbol + (inSymbol*(width - 2)) + outSymbol)
    
    if width != 1:
        print(outSymbol * width)


main()
