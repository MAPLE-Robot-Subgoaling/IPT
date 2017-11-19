def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxSymbol = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    if boxHeight == 1 and boxWidth == 1:
        print(boxSymbol)
    else:
        print(boxSymbol * boxWidth)
        for H in range(0, boxHeight -2):
            print(boxSymbol + (boxFill * (boxWidth -2))+ boxSymbol)
        print(boxSymbol * boxWidth)
main()
