def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    for h in range(height+1):
        currentLine = ''
        for w in range(width+1):
            if ((h != 0 and h != height) and (w != 0 and w != width)):
                currentLine += fillSymbol
            else:
                currentLine += outlineSymbol
        print(currentLine)
main()
