def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol1 = input("Please enter a symbol for the box outline: ")
    symbol2 = input("Please enter a symbol for the box to fill: ")
    for i in range(height):
        for j in range(width):
            print(symbol1 if i in [0, height-1] or j in [0, width-1] else symbol2, end = '')
        print()
main()
