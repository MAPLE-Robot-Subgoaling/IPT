
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    
    outline_symbol = input("Please enter a symbol for the box outline: ")
    fill_symbol = input("Please enter a symbol for the box fill: ")
    
    interior_rows = height - 2
    interior_width = width - 2

    print(outline_symbol * width)

    for n in range(0, (interior_rows)):
        print(outline_symbol + (fill_symbol * interior_width) + outline_symbol)
    
    
    print(outline_symbol * width)

main()
