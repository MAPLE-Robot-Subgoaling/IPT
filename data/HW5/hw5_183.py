def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    inside = (width - 2)
    for h in range(height, 0, -1):
        if(h == height):
            print(outline*width)
        elif(h == 1):
            print(outline*width)
        else:
            print(outline+(fill*inside)+outline)
main()
