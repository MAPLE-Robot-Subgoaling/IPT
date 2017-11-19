def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))
    for i in range(height):
        line = ""
        for k in range(width):
            if i == 0 or i == height-1:
                line = line + outline
            else:
                if k == 0 or k == width-1:
                    line = line + outline
                else:
                    line = line + fill
        print(line)
main()
