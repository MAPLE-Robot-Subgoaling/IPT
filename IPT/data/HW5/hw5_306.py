

def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline_symbol = str(input("Please enter a symbol for the box outine: "))
    filling_symbol = str(input("Please enter a symbol for the box fill: "))

    for i in range(height):

        if i == 0 or i == height - 1:
            print(outline_symbol * width)

        else:
            print(outline_symbol + filling_symbol*(width - 2) + outline_symbol)
        

main()

