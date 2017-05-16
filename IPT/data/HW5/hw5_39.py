

def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    for h in range(height):
        if h == 0 or h == height - 1:
            print(outline * width)

        else:
            print(outline + ((width - 2) * fill) + outline)

main()
