def main():
    var_boxWidth = int(input("Please enter the width of the box: "))
    var_boxHeight = int(input("Please enter the height of the box: "))
    var_boxOutline = str(input("Please enter a symbol for the box outline: "))
    var_boxFill = str(input("Please enter a symbol for the box fill: "))
    lst_Height = []
    for i in range(var_boxHeight):
        if i == 0 or i == var_boxHeight - 1:
            print(var_boxOutline * var_boxWidth)
        else:
            print(var_boxOutline + (var_boxFill * (var_boxWidth - 2)) + var_boxOutline)
main()
