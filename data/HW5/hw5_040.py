def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol of the box outline: ")
    fill = input("Please enter the symbol of the box fill: ")
    if height >= 1:
        print(outline * width)
    if width == 1:
        for i in range(height - 2):
            print(outline + fill * (width - 2))
    else:
        print(outline + fill * (width - 2) + outline)
    if height >= 2:
        print(outline * width)
main()
