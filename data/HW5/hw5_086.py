def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the box outline: ")
    filling = input("Please enter the symbol for the box fill: ")
    for i in range(height):
        toPrint = ""
        if i == 0 or i == height - 1:
            for n in range(width):
                toPrint = toPrint + outline
        else:
            for n in range(width):
                if n == 0 or n == width - 1:
                    toPrint = toPrint + outline
                else:
                    toPrint = toPrint + filling
        print(toPrint)
main()
