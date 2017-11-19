def main():
    width = int(input("Please enter the width of the box: "))
    hieght = int(input("Please enter the hieght of the box: "))
    outline = input("Please enter a symbol for the boc outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for i in range(0,hieght):
        if(i == 0 or i == hieght-1):
            print(outline*width)
        else:
            print(outline + fill*(width-2) + outline)
main()
