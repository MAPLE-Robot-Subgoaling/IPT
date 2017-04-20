
def main():
    
    width = int(input("Width of box: "))
    height = int(input("Height of box: "))
    outline = str(input("Symbol for box outline: "))
    fill = str(input("Symbol for box fill: "))

    for y in range (0, height):
        if (y == 0 or y == height-1):
            print(outline * width)
        else:
            print(outline + fill * (width - 2) + outline)

main()
