def main():
    box_width   = int(input("Please enter the width of the box: "))
    box_height  = int(input("Please enter the height of the box: "))
    box_outline = input("Please enter a symbol for the box outline: ")
    box_fill    = input("Please enter a symbol for the box fill: ")
    for draw in range(box_height):
        if   draw == 0:
            print (box_outline * box_width)
        elif draw == (box_height - 1):
            print (box_outline * box_width)
        else:
            print (box_outline + (box_fill * (box_width - 2)) + box_outline)
main()
