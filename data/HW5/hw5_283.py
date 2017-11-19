def main():
    width=int(input("Please enter the width of the box: "))
    height=int(input("Please enter the heigh of the box: "))
    outline=input("Please enter a symbol for the box outline: ")
    fill=input("please enter a symbol for the box fill: ")
    for b in range(1,height+1):
        if b==1 or b==height:
            print(outline*width)
        else:
            filler=width-2
            if filler>0:
                print(outline+(fill*filler)+outline)
            elif filler==0:
                print(outline*width)
main()
