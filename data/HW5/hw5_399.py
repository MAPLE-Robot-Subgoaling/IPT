def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    box = []
    for a in range(height):
        if a == 0 or a == height - 1:
            box.append(outline * width)
        else:
            box.append(outline + fill * (width - 2) + outline)
    for a in box:
        print(a)
main()
