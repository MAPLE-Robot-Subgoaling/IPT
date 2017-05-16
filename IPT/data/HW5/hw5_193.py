
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    boxTop = ""
    boxMid = ""
    boxBot = ""
    for i in range(width):
        boxTop += outSymbol
        boxBot += outSymbol
    boxMid += outSymbol
    for i in range(width - 2):
        boxMid += fillSymbol
    boxMid += outSymbol
    print(boxTop)
    for i in range(height - 2):
        print(boxMid)
    if height > 1:
        print(boxBot)

main()
