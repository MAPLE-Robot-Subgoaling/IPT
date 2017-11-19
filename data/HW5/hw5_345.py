def main():
    width = int(input("Pease enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = str(input("Please enter a symbol for the box outline: "))
    symbol1 = str(input("Please enter symbol for the box fill: "))
    for x in range(height):
        if x == 0 or x == (height -1):
            print(symbol * width)
        else:
            print(str(symbol) + (str(symbol1) *(width - 2)) + str(symbol))
main()
