
def main():

    width = int(input("Enter the width of your box: "))
    height = int(input("Enter the height of your box: "))
    outline = input("Enter the symbol for the outline: ")
    fill = input("Enter the symbol for the filling: ")
    for i in range(0, height):
        if(i == 0 or i == height - 1):
            print(outline * width)
        else:
            print(outline + "" + (fill * (width - 2)) + "" + outline)
        
main()
