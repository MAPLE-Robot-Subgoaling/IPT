def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))
    line = ""
    for h in range(0, height):
        if h == 0 or h == (height-1):
            print(outline*width)
        else:
            print(outline + (fill*(width-2)) + outline)
main()
