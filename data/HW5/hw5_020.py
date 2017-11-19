def main():
    width = int(input("Enter the width: "))
    height = int(input("Enter the hight: "))
    outline = input("Enter the symbol to outline with: ")
    fill = input("Enter the symbol to fill with: ")
    wide = ""
    filled = ""
    for n in range(0, height+1):
        for i in range(0, width+1):
            if i>0 and i<width+1:
                print(outline)
            else:
                print(fill)
main()
