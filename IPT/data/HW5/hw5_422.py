




def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))

    if height > 1:
        print(outline*width)
    for y in range(0, height-2, 1):
        print(outline + fill*(width-2) + outline)
    if (width > 1):
        print(outline*width)
        
    

main()
