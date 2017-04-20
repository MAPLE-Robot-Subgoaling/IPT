
def main():
    drawBox()

def drawBox():
    width = int(input("What is the width of the box? "))
    height = int(input("What is the height of the box? "))
    outline = input("What symbol would you like for the outline? ")
    fill = input("What symbol would you like for the fill? ")
    row = ""
    for y in range(height):
        if(y == 0 or y == range(height)[-1]):
            print(outline*width)
        else:
            for x in range(width):
                if(x == 0 or x == range(width)[-1]):
                    row = row + outline
                else:
                    row = row + fill
            print(row)
            row = ""
main()
