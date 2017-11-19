def main():
    width = int(input("Please enter the width of the box: " , ))
    height = int(input("Please enter the height of the box: " , ))
    outline = str(input("Please enter a symbol for the box outline: " , ))
    fill = str(input("Please enter a symbol for the box outline: " , ))
    for h in range(height):
        for w in range(width):
            print(outline if h in [0, height - 1] or w in [0, width - 1] else fill, end = "")
        print()
main()
