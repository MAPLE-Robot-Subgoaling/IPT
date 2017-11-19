def main():
    width = int(input("Please enter the width of the box:  "))
    height = int(input("Please enter the height of the box:  "))
    perimeter  = input("Please enter a symbol for the bout to outline")
    guts = input("please enter a symbol for the box to fill:  ")
    if( height != 1 and width !=1):
        print( width * perimeter)
        insideWidth =  width - 2
        insideHeight = height - 2
        for i in range (insideHeight):
            print(perimeter + (guts * insideWidth) + perimeter)
        print(width * perimeter)
    else:
        print(perimeter)
main()
