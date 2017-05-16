
def main():
    wDth = int(input("Please enter the width of the box: "))
    hIth = int(input("Please enter the height of the box: "))
    outLn = input("Please enter the character you'd like for the"
                  + " outline of the box: ")
    fill = input("Please enter the character you'd like for the" 
                 + " fill of the box: ")
    print (outLn*wDth)#Top
    for x in range(hIth-2):#Middle
        print (outLn,end="")
        print (fill*(wDth-2),end="")
        print (outLn)
    print (outLn*wDth)#Bottom
main()
