def main():
    width = int(input("Please enter the height of the box:"))
    height = int(input("Please enter the width of the box:"))
    outline = input("Enter the symbol for the outline")
    fill = input("Enter the symbol you wish to fill the box with:")
    for i in range(height):
        if i % height == 0 or i%height == height-1:
            print(outline*width)
        else:
            print(outline+fill*(width-2)+outline)
main()
