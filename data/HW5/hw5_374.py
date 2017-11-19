def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = input("Please enter the symbol for the box outline: ")
    filling = input("Please enter the symbol for the box filling: ")
    fillWidth = width - 2
    for box in range(1,height):
        if box == 1:
            print (symbol*width)
        else:
            print (symbol+(fillWidth*filling)+symbol)
    print(symbol*width)
main()
