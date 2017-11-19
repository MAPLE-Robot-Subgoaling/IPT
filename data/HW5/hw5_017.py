def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol1 = input("Please enter a symbol for the box outline: ")
    symbol2 = input("Please enter a symbol for the box fill: ")
    sentinel = 0
    inside = width - 2
    for s in range(0, height):
        if s == 0 or s == (height - 1):
            print(symbol1*width)
        else:
            print(symbol1 + (symbol2 * inside) + symbol1)
        sentinel = sentinel + 1
main()
