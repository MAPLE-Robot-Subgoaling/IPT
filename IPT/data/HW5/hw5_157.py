
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box to fill: ")

    if(height > 0 and width > 0):
        print(outline * width)
    if(width > 0):
        for i in range(height - 2):
            if(width > 1):
                print(outline + fill * (width - 2) + outline)
            else:
                print(outline)
    if(height > 1 and width > 0):
        print(outline * width)

main()
