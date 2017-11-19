def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    adjustedHeight = height - 2
    adjustedWidth = width - 2
    for n in range(1):
        print(outline * width)
    for n in range(adjustedHeight):
        print(outline + (fill * (adjustedWidth)) + outline)
    if height > 1:
        print(outline * width)
main()
