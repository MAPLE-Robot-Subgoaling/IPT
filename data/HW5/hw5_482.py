
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the outline: ")
    fill = input("Please enter the fill for the outline: ")

    for i in range(height):
 
        if i == 0 or i == (height - 1):
            print(outline * width)
        
        else:
            print(outline, fill * (width-2), outline)
        
main()
