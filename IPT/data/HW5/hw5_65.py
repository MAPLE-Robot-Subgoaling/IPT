
def main():

    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    outSymbol = input("Please enter a symbol for the box outline:")
    fillSymbol = input("Please enter a symbol for the box fill:")
    
    for i in range(0,height):
        wSymbol = outSymbol * width
        hSymbol = outSymbol + (fillSymbol * (width-2)) + outSymbol
        if i == 0 or i == height-1:
            print(wSymbol)
        else:
            print(hSymbol)
    
       
main()
