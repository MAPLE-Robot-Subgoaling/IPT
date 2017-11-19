def main():
    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    symbol = input("Please enter the symbol for the box outline:")
    fill = input("Please enter the symbol for the box fill")
    for h in range ( height):
        if h == 0 or h == height - 1:
            print(symbol * width)
        else:
            print(symbol + fill * ( width - 2 ) + symbol)
main()
