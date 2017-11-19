def main():
    height = int(input("Please enter the height of the box: "))
    width = int(input("Please enter the width of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for x in range(0, height):
        if x == 0 or x == (height - 1):
            print(outline * width)
        else:
            print(outline+(fill*(width - 2))+outline)
main()
