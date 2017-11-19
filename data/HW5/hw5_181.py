def main():
    width = int(input("Please enter the width of the box: "))
    height  = int(input("Please enter the height of the box: "))
    border = input("Please enter a symbol for the border of the box: ")
    content = input("Please enter a symbol for what is in the box: ")
    rows = [border * width, border + (content * (width - 2)) + border]
    for r in range(height):
        if r == 0 or r == height-1:
            print(rows[0])
        else:
            print(rows[1])
main()
