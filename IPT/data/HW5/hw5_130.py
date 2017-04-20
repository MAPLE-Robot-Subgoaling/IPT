
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    out = input("Please enter the symbol the box will be outlined in: ")
    fill = input("Please enter the symbol the box will be filled in with: ")

    for h in range(height, 0, -1):
        if h == height:
            print(width*out)
        if h > 1 and h < height:
            truWidth  = width-2
            print(out+truWidth*fill+out)
        if h == 1:
            print(width*out)

main()
