
def main():

    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
    symbolOutline = input("What symbol do you want for the outline? ")
    symbolFill = input("What symbol do you want to fill the box? ")

    if width > 1 and height > 1:
        print(symbolOutline*width)
        for i in list(range(height-2)):
            print(symbolOutline + symbolFill*(width-2) + symbolOutline)
        print(symbolOutline*width)
    else:
        print(symbolOutline)
        
main()
