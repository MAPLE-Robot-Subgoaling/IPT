
def main():
    
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol1 = input("Please enter a symbol for the box outline: ")
    symbol2 = input("Please enter a symbol for the box fill: ")
    WIDTH2 = width - 2
    HEIGHT2 = height - 2
    for s in symbol1:
        print(symbol1 * width)
        for y in range(HEIGHT2):
           print(symbol1 + symbol2 * WIDTH2 + symbol1)
        if height != 0:
           print(symbol1 * width)
            
main()
