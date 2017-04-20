def main():
    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    outline = input("Please enter a symbol for the box outline:")
    fill = input ("Please enter a symbol for the box fill:")
    for i in range (height):
        for x in range(width):
            print (outline if i in [0, height-1] or x in [0, width - 1] else fill, end="")
        print()
main()
