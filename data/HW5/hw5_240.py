def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for n in range(0, height):
        if(n == 0 or n == height-1):
            print(outline * width)
        else:
            width = width - 2
            print(outline+fill*width+outline)
            width = width + 2
main()
