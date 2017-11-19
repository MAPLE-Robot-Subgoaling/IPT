def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please ether the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for num in range(height):
        if num == 0 or num == height - 1:
            print(outline * width)
        else:
            print((outline + fill) + (fill * (width - 3)) + outline)
main()
