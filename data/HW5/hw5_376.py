def main():
    width = int(input("Enter the width of the box:"))
    height = int(input("Enter the height of the box:"))
    outline = input("Enter the symbol to use as an outline")
    fill = input("Enter the symbol to use as the filler")
    border = ""
    for i in range(width):
        border = outline + border
    print(border)
    middle = outline + (fill*(width-2)) + outline
    for i in range(height-2):
        print(middle)
    print(border)
main()
