def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    box = list(range(0,height))
    box2 = list(range(0,width))
    for i in box:
        for j in box2:
            if j == 0 or j == -1:
                i = symbol
                j = width
                print(i)
main()
