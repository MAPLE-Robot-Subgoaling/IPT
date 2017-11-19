def main():
    width = int(input("Enter width of box: "))
    height = int(input("Enter height of box: "))
    symbolOut = input("Enter a symbol for the outline: ")
    symbolIn = input("Enter a symbol for the filling: ")
    for i in range(height):
        if i == 0 or i == height - 1:
            print(symbolOut * width)
        else:
            print(symbolOut + (symbolIn * (width - 2)) + symbolOut)
main()
