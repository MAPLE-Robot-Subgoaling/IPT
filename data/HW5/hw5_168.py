def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    perimSym = input("Please enter a symbol for the box outline: ")
    areaSym = input("Please enter a symbol for the box area: ")
    for h in range(height + 1) :
        if h == 0 :
            print(perimSym * width)
        elif h > 0 and h < height - 1 :
            print(perimSym + areaSym * (width - 2) + perimSym)
        elif h == height and height == 1 :
            h = height + 2
        elif h == height :
            print(perimSym * width)
main()
