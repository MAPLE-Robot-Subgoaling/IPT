def main():
    boxWidth = int(input("Please enter the width of your box: "))
    boxHeight = int(input("Please enter the height of your box: "))
    boxOutline =  input("Please enter the symbol to outline your box with: ")
    boxFill = input("Please enter the symbol to fill your box with: ")
    print(boxOutline * boxWidth)
    for i in range(boxHeight - 2):
        print(boxOutline + boxFill * (boxWidth - 2)+ boxOutline)
    if boxHeight > 1:
        print(boxOutline * boxWidth)
main()
