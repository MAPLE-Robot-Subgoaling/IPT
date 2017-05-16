def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    boxFill= input("Please enter a symbol for the box fill: ")
    s =""
    for h in range(0,height):
        for w in range(0,width):
            if h== 0 or h == height-1 or w== 0 or w== width -1:
                s = s + outline
            else:
                s = s + boxFill
        s = s + "\n"
    print(s)

main()
