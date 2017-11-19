def main():
    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    border = input("Please enter the sybol the box will be out lined in:")
    fill = input("Please enter the symbol the box will be filled in:")
    x=0
    y=0
    printingString=""
    while(x!=width):
        printingString=printingString+border
        x=x+1
    print(printingString)
    x=0
    y=y+2
    while(y<height):
        printingString=""
        printingString=printingString+border
        x=x+2
        while(x<width):
            printingString=printingString+fill
            x=x+1
        x=0
        printingString=printingString+border
        print(printingString)
        y=y+1
    x=0
    y=0
    printingString=""
    while(x!=width):
        printingString=printingString+border
        x=x+1
    print(printingString)
main()
