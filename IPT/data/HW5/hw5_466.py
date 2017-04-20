
def main():
    width = int(input("Please enter the width of the box: "))

    height = int(input("Please enter the height of the box: "))

    outline_char = input("Please enter a symbol for the box outline: ")

    fill_char = input("Please enter a symbol for the box fill: ")

    for line in range(0, height):

        if line == 0 or line == height - 1:
            print(outline_char * width)
        else:
            print(outline_char + (fill_char * (width - 2)) + outline_char)

main()
