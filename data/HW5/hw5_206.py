def main():
    THICKNESS = 2
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol that will make up the outline of the box: ")
    fill = input("Please enter the symbol that will fill the box: ")
    realWidth = width-THICKNESS
    fillList = range(0,height)
    for n in fillList:
        if n == 0:
            print(outline*width)
        elif n == fillList[height-1]:
            print(outline*width)
        else:
            print(outline+(fill*realWidth)+outline)
main()
