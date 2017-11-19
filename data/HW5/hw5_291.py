def main():
    width = int(input("Please enter the width of the box:" ))
    height = int(input("Please enter the height of the box:" ))
    outline = input("Please enter a symbol for the box outline:" )
    filler = input("Please enter a symbol for the box fill:" )
    if height == 1:
        print(outline)    
    print(outline*width)
    for i in range(height-2):
        print(outline + (width-2)*filler + outline)
    print(outline*width)
main()
