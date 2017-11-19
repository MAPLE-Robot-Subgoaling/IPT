def main():
    width = input("Please enter the width of the box: ")
    width = int(width)
    height = input("Please enter the height of the box: ")
    height = int(height)
    middle = width - 2
    middle = int(middle)
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    endLine = outline * width
    inside = outline + (fill * middle) + outline
    print(endLine)
    for line in range(0, height - 2):
        print(inside)
    print(endLine)
main()
