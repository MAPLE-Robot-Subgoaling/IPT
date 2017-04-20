
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))

    print(outline * width)
    for i in range(0, height-2):
        print(outline + ((width - 2) * fill) + outline)
        
    print(outline * width)

main()
