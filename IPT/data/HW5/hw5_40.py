
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the box outline: ")
    filler = input("Please enter the symbol for the box outline: ")
    INSIDE = width - 2
    
    for h in range(height):
        if h == 0 or h == height - 1:
            print(outline*width)
        else:
            print(outline + filler*INSIDE + outline)
    print()

main()
