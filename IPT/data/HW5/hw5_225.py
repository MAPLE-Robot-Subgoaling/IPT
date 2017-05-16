
def main():
    width = int(input("What do you want the width of the box to be? "))
    height = int(input("What do you want the height of the box to be? "))
    outline = str(input("Enter the symbol you want the outline to be: "))
    fill = str(input("Enter the symbol you want the filling of the box to be: "))
    print(outline * width)
    if width > 2 and height != 1:
        filling = outline + fill *(width - 2) + outline
        for i in range(0, height - 2):
            print(filling)
    if width > 1 and height != 1:
        if width == 2:
            for i in range (0, height - 1):
                print(outline * width)
        else:
            print(outline * width)
    if width == 1 and height != 1:
        for i in range(0, height - 1):
            print(outline)
main()
