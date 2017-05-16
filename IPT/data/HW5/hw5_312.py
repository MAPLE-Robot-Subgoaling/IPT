
def main():
    width = input("Please enter the width of the box: ")
    width = int(width)
    height = input("Please enter the height of the box: ")
    height = int(height)
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter symbol for the box to be filled with: ")
    print(outline*width)
    if(height > 1):
        if(height > 2):
            for i in range(height-2):
                print(outline + (fill*(width-2)) + outline)
        print(outline*width)

main()
