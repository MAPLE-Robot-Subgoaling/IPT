def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolO = input("Please enter a symbol for the box outline: ")
    symbolI = input("Please enter a symbol for the inside of the box: ")
    firstline = (symbolO * width)
    lastline = firstline
    midlines = (str(symbolO)+ str(symbolI*(width-2))+ str(symbolO))
    print()
    print(firstline)
    for i in range(height - 2):
        print(midlines)
    if height > 1:
        print(lastline)
    print()
main()
