def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for i in range(height):
        if i == 0:
            print(outline * width)
        elif i != 0 and i != height - 1:
            print(outline + fill * (width - 2) + outline)
        else:
            print(outline * width)
main()
