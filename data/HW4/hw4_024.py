def main():
    EVEN=1
    STOP=1
    height=int(input("Please enter the starting height of the hail: "))
    while height != STOP:
        mod=height%2
        if mod == EVEN:
            height=((height*3)+1)
            print("The height is", height)
        else:
            height=height/2
            print("The height is", height)
    print("The hail stopped at height 1")
    height=STOP
main()
