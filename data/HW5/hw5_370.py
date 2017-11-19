def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    inside = width - 2
    for h in range(0 , height):
        if h == height - 1 or h == 0:
            print(width*outline)
        else: 
            print(outline + (inside * fill) + outline)
main()
