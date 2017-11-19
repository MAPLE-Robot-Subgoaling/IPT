def main():
    width = int(input("Please enter the width of the box: ")) 
    height = int(input("Please enter the height of the box: ")) 
    symbol = input("Please enter a symbol for the box outline: ")
    symbol_2 = input("Please enter a symbol for the box fill: ")
    for n in range(height):
        if n == 0 or n == height - 1:
            print(symbol * width)
        else:
            print(symbol + (symbol_2 * (width - 2)) + symbol)
main()
