def main():
    width = int(input("Please enter the width of the box:"))
    height = int(input("PLease enter the height of the box:"))
    outline = input("Please enter a symbol for the box outline:")
    fill = input("Please enter a symbol for the box fill:")
    for x in range (0,height):
        for y in range (0,width):
            if x == 0 or y == 0 or x == height-1 or y == width-1 :
                print(outline, end="")
            else:  
                print(fill,end="")
        print('')
main()
