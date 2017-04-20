
def main():
    box_width = int(input("Please enter the width of the box: "))
    box_height = int(input("Please enter the height of the box: "))
    box_symbol_outline = input("Please enter a symbol for the box outline: ")
    box_symbol_fill = input("Please enter a symbol for the box fill: ")

    for row in range(box_height):
        if row == 0 or row == box_height - 1:
            print (box_symbol_outline * box_height)
        else:
            print(box_symbol_outline + (box_symbol_fill * (box_height - 2)) 
                  + box_symbol_outline)
main()
