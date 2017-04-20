
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol to outline the box: ")
    fill = input("Please enter the symbol to fill the box: ")

    print(outline * width)
    if (height > 1):
        for h in range(0, height - 2, 1):
            if (width > 2):
                print(outline + fill * (width - 2) + outline)
            else:
                print(outline * width)
    if (height > 1):
        print(outline * width)
main()
