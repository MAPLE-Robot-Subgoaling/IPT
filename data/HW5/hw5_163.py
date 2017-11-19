def main():
    width = int(input("PLease enter the width of the box:  "))
    height = int(input("Please enter the height of the box:  "))
    outline = str(input("Please enter a symbol for the bo outline:  "))
    fill = str(input("Please enter a symbol for the box fill:  "))
    for num in range(height):
        if num == 0 or num == height - 1:
            print(outline*width)
        else:
            print(outline+((width-2)*fill)+outline)
main()              
