
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    height = height - 2
    topBot = width * outline
    print(topBot)
    for i in range(0,height):
        print(outline + ((width - 2) * fill) + outline)
    print(topBot)
main()
