def main():
    width  = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    out    = input("Please enter a symbol for the box outline: ")
    fill   = input("Please enter a symbol for the box fill: ")
    print(out * width)
    for i in range(height - 2):
        print(out + (fill * (width - 2)) + out)
    if height > 1:
        print(out * width)
main()
