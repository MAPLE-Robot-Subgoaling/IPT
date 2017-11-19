def main():
    width   = int(input("Please enter the width of the box: "))
    height  = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill    = input("Please enter a symbol for the box fill: ")
    outLen  = 2
    for i in range(height):
        if i == 0 or i == height-1:
            print(width * outline)
        else:
            print(outline + (fill*(width-outLen)) + outline)
main()
