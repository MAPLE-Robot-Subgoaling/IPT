def main():
    widthBox =int(input("Please enter the width of the box: "))
    heightBox =int(input("Please enter the height of the box: "))
    boxOut = input("Please enter a symbol for the box outline: ")
    boxIn = input("Please enter a symbol for the box fill: ")
    
    if(widthBox != 1) and (heightBox != 1):
        for a in range (0, 1):
            print(widthBox * boxOut)
        for a in range(1, heightBox-1):
            print((boxOut + (int(widthBox) - 2) * boxIn) + boxOut)
        print(widthBox * boxOut)
    else:
        print(boxOut)
main()
