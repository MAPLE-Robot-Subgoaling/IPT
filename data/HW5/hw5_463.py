
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSymbol = input("Please enter a symbol for the box outline: ")
    inSymbol = input("Please enter a symbol for the box fill: ")


    for i in range(height):
        if(i == 0 or i == height-1):
            print(outSymbol * width)
        
        else:
            print(outSymbol + inSymbol * (width - 2) + outSymbol)
    
main()

