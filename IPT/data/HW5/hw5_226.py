def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a sumbol for the box fill: "))
    print(outline*width)
    for counter in range(0,height-2):
        print(outline+fill*(width-2)+outline)
    if height >1:
        print(outline*width)
main()
