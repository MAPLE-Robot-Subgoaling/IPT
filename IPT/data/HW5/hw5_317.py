
def main():


    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = input("Please enter a symbol for the box perimeter: ")
    inner_symbol = input("Please enter a symbol for the box's inside: ")

    if width > 1 and height > 1:
        
        row1 = symbol * width
        print(row1)

        if height >= 2: 

            for row in range(0, height - 2):
            
                if width > 1:

                    mid_row = symbol + (inner_symbol * (width - 2)) + symbol
                    print(mid_row)

                elif width == 1:
                    mid_row = symbol
                    print(mid_row)

        row_final = symbol * width
        print(row_final)

    elif width == 1 or height == 1:
        for row in range(0, height):
            print(symbol * width) 

    else:
        print()

main()
