def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = list(str(input("Please enter a symbol for the box outline: ")))
    fill = str(input("Please enter a symbol for the box fill: "))
    if width == 1  and height == 1:
        print(outline)
    for i in outline:
        print(i * width)
        print(((i + (fill * (width - 2)) + i) + '\n') * (height - 2))
        print(i * width)
main()
