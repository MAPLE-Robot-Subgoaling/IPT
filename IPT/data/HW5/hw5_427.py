
def main():

    width = int(input("Please input the width "))

    height = int(input("Please input the height "))

    outSymbol = input("Please provide a symbol for the borders ")

    inSymbol = input("Please provide a symbol for the interior ")

    newHeight = height - 2
    

    print(width * outSymbol)
    
    for c in range(0, newHeight):
        if c > 0 or c < newHeight:
            print(outSymbol + (width-2) * inSymbol + outSymbol)
   
    print(width * outSymbol)
           
    

main()
