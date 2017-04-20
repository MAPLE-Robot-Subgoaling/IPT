
def main():
    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of box: "))
    outline = input("Enter a symbol for box outline: ")
    fill = input("Enter a symbol to fill box: ")
    print(outline*width)
    for row in range(height-2):
        print(outline+((width -2)*fill)+outline)
    print(outline*width)
    

main()
