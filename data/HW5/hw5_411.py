def main():
    width = int(input("please enter the width of the box: "))
    height = int(input("please enter the height of the box: "))
    outline = input("please enter a symbol for the box outline: ")
    fill = input("please enter a symbol for the box fill: ")
    for h in range(0, height):
        line = ""
        for w in range(width):
            if((h == 0) or (h == height-1) or (w == 0) or (w == width-1)):
                line = line + outline
            else:
                line = line + fill
        print(line)
main()
