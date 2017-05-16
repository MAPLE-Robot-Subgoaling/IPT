def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the box outline : ")
    fill = input("Please enter the symbol for the box fill : ")
    for i in range(0,height):
    
        for j in range(0,width):
            if i == 0:
                print(outline, end='')
            elif j==0:
                print(outline,end='')
            elif j == width-1:
                print(outline)
            elif i == height-1:
                print(outline,end='')
            else:
                print(fill ,end='')
        print("\n")
main()
