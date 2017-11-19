def main():
    userWidth = int(input("Please enter the width of the box:"))
    userHeight = int(input("Please enter the height of the box:"))
    boxOut = input("Please enter a symbol for the box outline:")
    boxFill = input("Please enter a symbol for the box fill:")
    for boxHeight in range(0,userHeight):
        if boxHeight == 0 or boxHeight == userHeight-1:
            print(boxOut*userWidth)
        else:
            print(boxOut+ boxFill*(userWidth-2)+ boxOut)
main()
