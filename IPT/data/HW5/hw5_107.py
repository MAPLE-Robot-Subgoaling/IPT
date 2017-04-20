
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the outline of the box: ")
    fill = input("Please enter a symbol for the fill of the box: ")
    
    for r in range(height):
        if r >= 1 and r <= height - 2:
            print(outline + (fill * (width - 2)) + outline)
        else:
            print(outline * width)
main()

