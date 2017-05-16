
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    border = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    print(border*width)
    for r in range(height - 2):
        print(border + fill*(width-2) + border)
    print(border*width)
main()
