def main():
    w = int(input("Please enter the width of the box: "))
    h = int(input("Please enter the height of the box: "))
    o = input("Please enter a symbol for the box outline: ")
    f = input("Please enter a symbol for the box fill: ")
    for s in range(0,1):
        print(o*w)
        if w != h:
            for a in range(0,(h-2)):
                print((o + f) + (f*(w-4)) + (f+o))
            print(o*w)
main()
