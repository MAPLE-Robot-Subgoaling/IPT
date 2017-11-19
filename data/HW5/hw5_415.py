def main():
    width = int(input("Please enter the width: "))
    height = int(input("Please enter the height: "))
    outSymbol = input("Please enter the outlining symbol: ")
    inSymbol = input("Please enter the inner symbol: ")
    if (width)!=1 and (height)!=1:
        print((outSymbol)*(width))
        newWidth = (width)-2
        newHeight = (height)-2
        for n in range(newHeight):
            print((outSymbol)+((inSymbol)*(newWidth))+(outSymbol))
        print((outSymbol)*(width))
    else:
        print(outSymbol)
main()
