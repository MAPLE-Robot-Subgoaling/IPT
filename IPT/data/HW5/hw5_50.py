
def main():


    boxWidth = int(input("What is rhe desired width of the box? "))
    boxHeight = int(input("What is the desired hight of the box? "))
    boxBorder = input("What is the desired border of the box? ")
    boxFill = input("What is the desired interior of the box? ")

    horizontal  = boxBorder + (boxFill * (boxWidth - 2)) + boxBorder
    center = [horizontal] * (boxHeight - 2)
    vertical = [boxBorder] * (boxHeight - 2)

    print (boxBorder * boxWidth)
    if boxWidth == 1:
        for w in vertical:
            print (w)
    else:
        for w in center:
            print(w)
    if boxHeight > 1:
        print(boxBorder * boxWidth)
main()
