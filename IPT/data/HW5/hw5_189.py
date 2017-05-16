ZERO = 0
START = 0
STEP = 1
HEIGHT_ADJUST = -1
WIDTH_ADJUST = -2
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol fot the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    row = START
    for row in range(START, height, STEP):
        if(row == ZERO or row == (height + HEIGHT_ADJUST)):
               print((outline)*(width))
        else:
               print(outline + fill*(width + WIDTH_ADJUST) + outline)

    
main()
