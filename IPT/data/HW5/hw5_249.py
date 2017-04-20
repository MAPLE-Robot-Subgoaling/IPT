
def main() :
    w = int(input("Please enter the width of the box: "))
    h = int(input("Please enter the height of the box: "))
    out = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for i in range(0,h) :
        if(i == 0 or i == (h-1)) :
            print(out*w)
        else :
            print(out + fill*(w-2) + out)

main()
