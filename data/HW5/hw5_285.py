def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for column in range(0,height):
        if (column == 0 or column == height-1):
            print(outline*width)
        else:
            print (outline + fill*(width-2) + outline)
main()
