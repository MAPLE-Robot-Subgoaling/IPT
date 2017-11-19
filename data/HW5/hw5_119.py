def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol_outline = input("Please enter a symbol for the box outline: ")
    symbol_fill = input("Please enter the symbol for the box fill: ")
    fillspace = " "
    for h in range(height):
        if h == 0 or h == height - 1: 
            print(width * symbol_outline)
        else:
            print(symbol_outline + fillspace * (width - 2) + symbol_outline)
            for w in range(height - 2):
                if w == 0 or w == height - 2:
                    print((width - 2) * symbol_fill)
                else:
                    print(symbol_fill * (width - 4)) 
main()
