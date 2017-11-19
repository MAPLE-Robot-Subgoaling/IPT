def main():
    width = int(input("Please enter the width of the box "))
    height = int(input("Please enter the height of the box "))
    boxoutline =input("Please enter a symbol for the box outline ")
    boxfill = input("Please enter a symbol for the box fill ")
    for i in range (0,height):
        if (i==(height-1) or (i==0)):
            print(boxoutline * width)
        else:
            print(boxoutline+boxfill * (width-2) + boxoutline)
main()
