def main():
    width = int(input('Please enter the width of the box: '))
    height = int(input('Please enter the height of the box: '))
    outline = input('Please enter a symbol for the box outline: ')
    fill = input('Please enter a symbol for the box fill: ')
    if (width == 1 and  height == 1):
        print(outline)
    else:
        print(outline*width)
        for i in range((height-2)):
            print(outline + fill*(width-2) + outline)
        print(outline*width)
main()
