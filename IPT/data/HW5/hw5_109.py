
def main():
    widthBox = int(input("Please enter the width of the box:"))
    heightBox = int(input("Please enter the height of the box:"))
    symbolOutlined = input("Please enter a symbol for the box ouline:")
    symbolFilled = input("Please enter a symbol for the box fill:")
    combine = symbolOutlined + (symbolFilled * (widthBox -2)) + symbolOutlined
    for everyline in range(heightBox): #Repeat for each # in range of height
        if everyline == 0 or everyline == (heightBox - 1):            
            print(symbolOutlined* widthBox)
        else:            
            print(combine)
main()
