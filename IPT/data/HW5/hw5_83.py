


def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlined = input("Please enter a symbol for the box outline: ")
    filled = input("Please enter a symbol for the box fill: ")

    print(outlined * width)
    for n in range (0, height-2):
        print((outlined) + (filled*(width-2)) + (outlined))
    print(outlined*width)
main()
