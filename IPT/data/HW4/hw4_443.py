


def main():
    Height = 2
    Height = int(input("Please enter the starting height of the hailstone: "))
    EVEN = 0
    ODD = 1
    LASTNUMBER =1
    while Height != LASTNUMBER:    
        Decider = Height%2
        while Decider == EVEN and Height !=LASTNUMBER:
            Height = ((Height/2))
            print("Hail is currently at height", Height)
            Decider = Height%2
        while Decider == ODD and Height !=LASTNUMBER:
            Height = ((Height*3)+1)
            print("Hail is currently at height", Height)
            Decider = Height%2
main()
