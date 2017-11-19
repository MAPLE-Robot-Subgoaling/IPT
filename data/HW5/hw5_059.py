def main():
    length = int(input("Please enter the width of the box: "))
    lines = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the outline of the box: ")
    fill = input("Please enter a symbol for the box to fill: ")
    for i in range(lines):
        if i == 0 or i == (lines-1):
            print(outline*length)
        else:
            print(outline+(fill * (length -2))+outline)
main()
