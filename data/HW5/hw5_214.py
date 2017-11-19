def main():
    width = int(input("PLease enter the width of the box: "))
    height = int(input("PLease enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    line = ""
    for i in range(0, height+1):
        if(i != 0):
            print(line)
            line = ""
        for a in range(0,width):
            if i == 0 or i == height-1:
                line = line+outline
            else:
                if a == 0 or a==width-1:
                    line = line+outline
                else:
                    line = line+fill
main()
