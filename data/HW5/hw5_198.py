def main():
    width = int(input("please enter the width of the box: "))
    height = int(input("please enter the height of the box: "))
    boxOutline = (input("please enter a symbol for the box outline: "))
    boxFilling = (input("please enter a symbol for the box fill: "))
    for i in range(height):
        if i == 0 or i == (height-1):
            print((boxOutline)*(width))
        else:
            print((boxOutline)+(boxFilling * (width - 2))+(boxOutline))
main()
