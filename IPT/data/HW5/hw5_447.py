
def main():
    
    width = int(input("Please enter the width of the box:",))
    height = int(input("Please enter the height of the box:",))
    outline = input("Please enter a symbol for the box outline:",)
    inFill = input("Please enter a symbol for the box fill:",)

    if height > 1:
        
        print(outline*width)
        for i in range(height-2):
        
            print(outline + inFill*(width-2) + outline)
        print(outline*width)

    elif height == 1:
        
        print(outline*width)

main()
