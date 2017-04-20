
def main():
    widthBox = input("Please enter the width of the box: ")
    heightBox = input("Please enter the height of the box: ")
    widthBox = int(widthBox)
    heightBox = int(heightBox)
    boxOut = input("Please enter the symbol for the box outline: ")
    boxIn = input("Please enter the symbol for the box fill: ")
    for i in range(heightBox):
        if i == 0 or i == heightBox - 1:
            print(widthBox * boxOut)
        else:
            print(boxOut + boxIn * (widthBox - 2) + boxOut)
main()
