
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    for y in range(height):
        if (y == 0 or y == height - 1):
            line = outline * width
        else:
            if (width <= 2):
                line  = outline * width
            else:
                line = outline + fill * (width - 2) + outline
        print(line)

main()
