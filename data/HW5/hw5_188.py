def main():
    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
    outline = input("Enter a symbol for the box outline: ")
    fill = input("Enter a symbol for the box fill: ")
    print (outline * width)
    for i in range (height-2):
            print (outline + fill * (width - 2) + outline)
    print (outline * width)
main()
