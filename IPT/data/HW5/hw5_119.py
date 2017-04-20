def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSym = input("Please enter a symbol for the box outline: ")
    fillSym = input("Please enter a symbol for the box fill: ")
    for line in range(height):
        if line == 0 or line == height-1:
            print(outlineSym*width)
        else:
            if width>2:
                fill = fillSym*(width-2)
                print(outlineSym+fill+outlineSym)
            elif width==1:
                print(outlineSym)
            else:
                print(outlineSym*2)
main()
