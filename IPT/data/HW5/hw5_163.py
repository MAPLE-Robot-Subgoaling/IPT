
def main():

    width = int(input("Please enter width of box: "))
    height = int(input("Please enter height of box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    print(width * outline)
    for n in range(0, height - 2):
        print(outline  + fill * (width - 2) + outline)
    if height != 1:
        print(outline * width)

main()
