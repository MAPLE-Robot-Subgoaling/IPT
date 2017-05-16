
def main():

    OUTLINE_WIDTH = 2

    width  = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))

    charOutline = input("Please enter the symbol for the box outline: ")
    charFill    = input("Please enter the symbol for the box fill: ")

    line = ""

    for i in range(height):

        if i == 0 or i == height - 1:
            line = charOutline * width

        else:
            line = charOutline + charFill * (width - OUTLINE_WIDTH) + charOutline

        print(line)



main()
