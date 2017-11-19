def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOut = input("Please enter the symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    w = boxWidth
    h = boxHeight
    o = boxOut
    f = boxFill
    print(w*(o))
    for h in range(boxHeight):
        print(o*(1) + f*(w-2) + o*(1))
    print(w*(o))
main()
