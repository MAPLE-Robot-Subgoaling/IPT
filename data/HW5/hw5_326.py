def main():
    symbolString = ""
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    widthRange = width - 2
    for i in range(height):
        symbolString = ""
        if i == 0 or i == height - 1:
            for n in range(width):
                symbolString += outline
            print(symbolString)
        else:
            symbolString += outline
            for q in range(widthRange):
                symbolString += fill
            symbolString += outline
            print(symbolString)
main()
