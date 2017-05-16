

def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outSym = input("Please enter a symbol for the box outline: ")
    fillSym = input("Please enter a symbol for the box fill: ")
    num = width - 2
    for i in range(height):
        if i == 0 or i == height-1:
            print(outSym * width)
        else:
            print(outSym+fillSym*num+outSym)
main()
