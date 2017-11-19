def main():
    width = int(input("What is the width of your box?: "))
    height = int(input("What is the height of your box?: "))
    symbolOutline = input("What symbol is the outline of the box?: ")
    symbolFill = input("What symbol is the inside of the box?: ")
    row = ""
    for i in range(height):
        for j in range(width):
            if i == 0 or i == (height - 1):
                row = row + symbolOutline
            else:
                if j == 0 or j == (width - 1):
                    row = row + symbolOutline
                else:
                    row = row + symbolFill
        print(row)
        row = ""
main()
