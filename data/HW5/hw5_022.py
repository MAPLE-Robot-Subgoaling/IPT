def main():
    boxLen = eval(input("Please enter the width of the box: "))
    boxWid = eval(input("Please enter the height of the box: "))
    boxBorder = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    for i in range(boxLen):
        if (i == 0 or i == (boxLen - 1)):
            print((boxBorder + "") * boxWid)
        else:
            print(boxBorder , boxFill* (boxWid - 2)  , boxBorder)
main()
