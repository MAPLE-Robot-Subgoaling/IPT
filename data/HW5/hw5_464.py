def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol_outline = input("Please enter a symbol for the box outline: ")
    symbol_fill = input("Please enter a symbol for the box fill: ")
    height_list = [0]
    height_counter = 1
    print()
    for a in height_list:
        if len(height_list) != height:
            height_list.append(height_counter)
            height_counter = height_counter + 1
    for row in height_list:
        if row == 0 or row == height - 1:
            print(symbol_outline * width)
        else:
            print(symbol_outline + (symbol_fill * (width - 2)) + symbol_outline)
    print()
main()
