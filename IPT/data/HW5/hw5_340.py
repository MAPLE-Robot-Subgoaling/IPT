
def main():
    w = int(input("Please enter the width of the box: "))
    h = int(input("Please enter the height of the box: "))

    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    for i in range(h):
        if i == 0 or i == h - 1:
            print(outline * w)
        else:
            print(outline + (fill * (w - 2)) + outline)

main()
