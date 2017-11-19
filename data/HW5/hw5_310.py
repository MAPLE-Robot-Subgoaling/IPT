def main():
    width = int(input("Please input the width of the box: "))
    height= int(input("Please input the height of the box: "))
    symout = input("Please input the symbol you want outlined: ")
    symfil = input("Please input the symbol you want to use to fill in: ")
    for i in range (height,0, -1):
        if i  == height:
            top = symout*width
            print(top)
        if i >1 and i < height:
            newwidth = width-2
            middle = symfil*newwidth
            print(symout+middle+symout)
        if i == 1:
            bottom = symout * width
            print(bottom)
main()
