def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the box outline: ")
    fill = input("Please enter the symbol for the box fill: ")
    outline = width*outline
    print(outline)
    fill = fill*(width-2)
    for i in range(2, height):
        slicedOutline = outline[1]
        print(slicedOutline+fill+slicedOutline)
    if height > 1:
        print(outline)
main()
