def main():
    width = int(input("Please enter the width of the desired box: "))
    height = int(input("Please enter the height of the desired box: "))
    outline = input("Now, please enter a symbol for the box outline: ")
    fill = input("Finally, please enter a symbol for the box filler: ")
    print (outline * width)
    if (height - 2) >= 1:
        for i in range (height - 2):
            print (outline + (fill * (width - 2)) + outline)
        print (outline * width)
    elif (height - 2) == 0:
        print (outline*width)
main()
