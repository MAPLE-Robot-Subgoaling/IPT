
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the lenght of the box: "))
    symbol = input("Please enter a symbol for the box outline: ")
    symbol_fill = input("Please enter a symbol for the box fill: ")

    for i in range(height):
        if i == 0 or i == height-1:
            print(symbol*width)
        else:
            print(symbol + symbol_fill*(width-2) + symbol)
    

main()
