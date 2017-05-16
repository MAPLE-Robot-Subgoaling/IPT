def main():
    width = int(input("Please input the width: "))
    height = int(input("Please input the height: "))
    outline = input("What is the symbol for the box outline? ")
    filling = input("What is the symbol for the filling of the box? ")
    print(outline * width)
    for j in range(0,height -2):
        print(outline+filling*(width-2)+outline)
    print(outline*width)
main()
