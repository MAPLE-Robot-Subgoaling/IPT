def main():
    Width = int(input("Please enter the width of the box: "))
    Height = int(input("Please enter the height of the box: "))
    Bout = input("Please enter a symbol for the box outline: ")
    Bfill = input("Please enter a symbol for the box fill: ")
    for i in range(Height):
        if i == 0:
            print(Bout*Width)
        elif i == Height-1:
            print(Bout*Width)
        else: 
            print((Bout)+(Bfill*(Width-2))+(Bout))
main()
