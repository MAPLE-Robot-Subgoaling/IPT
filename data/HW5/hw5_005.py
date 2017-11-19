def main():
    print("This program will draw a box using given dimensions.")
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    print(outline*width)
    for n in range(1,(height-1)):
        print(outline + (fill*(width-2)) + outline)
    if height != 1:
        print(outline*width)
main()
