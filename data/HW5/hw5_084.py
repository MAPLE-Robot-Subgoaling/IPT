def main():
    length = int(input("Enter your length of the triangle: "))
    width = int(input("Enter your width: "))
    outline = input("Please enter a symbol for outline: ")
    filler = input("Please enter a symbol to fill the box: ")
    inner_size = length - 2
    print (outline * length)
    def printRect (length,width,outline,filler):
        for i in range(inner_size):
            print (outline + filler * inner_size + outline)
    printRect(length,width,outline,filler)
main()
