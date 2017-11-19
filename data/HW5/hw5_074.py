def main():
    width = int(input("Please enter the width of your box: "))
    height = int(input("Please enter the height of your box: "))
    outline = input("Please enter the symbol of your outline: ")
    filling = input("Please enter the symbol for your filling: ")
    for n in range(1,height + 1):
        if n == 1  or  n == height:
            print(outline * width)
        else:
            print(outline + filling * (width - 2) + outline)
main()
