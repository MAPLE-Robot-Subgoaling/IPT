def main():
    width= int(input("Please enter the width of your box:"))
    length= int(input("Please enter the length of your box:"))
    outsideSymbol = input("Please enter the symbol that will outline your box:")
    insideSymbol = input("Please enter the symbol that will fill the inside of your box:")
    outlineOfBox = outsideSymbol * width
    print(outlineOfBox)
    for i in range(0:len(outlineOfBox)-1):
        print(outsideSymbol *(length - 2))
    for i in range(1 , len(outlineOfBox)-1):
            print((insideSymbol * (length-2))+ outsideSymbol)
main()
