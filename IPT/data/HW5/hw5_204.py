def main():
    width = int(input(" Please enter the width of the box:  "))
    height = int(input(" Please enter the height of the box:  "))
    symbol_o = input(" Please enter a symbol for the box outline:  ")
    symbol_i = input(" Please enter a symbol for the box fill:  ")
    height = height - 2
    if height <= 1 and width <= 1:
        print(symbol_o)
    elif width == 2 and (height + 2) == 2:
        print(symbol_o + symbol_o)
        print(symbol_o + symbol_o)
    elif height <= 1:
        print(symbol_o + symbol_i * (width - 2) + symbol_o)
    elif width <= 1:
        for w in range(0,(height + 2)):
            print(symbol_o)    
    else :
        print(symbol_o * width)
        for w in range(0,height) :
            print(symbol_o + (symbol_i * (width - 2)) + symbol_o)
        print(symbol_o * width)
  
main()
