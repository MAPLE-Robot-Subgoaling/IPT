def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))
    inside = width - 2
    for i in range(1, height+1, 1):
        print(outline*height, inside*fill, width*outline)
main()
