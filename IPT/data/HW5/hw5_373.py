
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSymbol = input("Please enter a symbol for the box outline: ")
    inSymbol = input("Please enter a symbol for the box fill: ")
    
    
    print(width*outSymbol)
    for i in range(0, height-2):
        print (outSymbol + ((width-2)*inSymbol) + outSymbol)
    for i in range(1, height):    
        print(width*outSymbol)

main()
