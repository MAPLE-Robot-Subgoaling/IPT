def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the bow: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the bow fill: ")
    for h in range(height):
        if h == 0 or (height - h) ==1:
            line = outline*width
            print(line)
        else:
            if width > 1:
                inside = outline+ (fill*(width-2))+ outline
                print(inside)
            else:
                print(outline)
main()
