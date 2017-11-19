def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    if( height == 1 ):
        print("The hailstone doesn't move from this height")
    else:
        while( height != 1 ):
            if( height % 2 == 0 ):
                height //= 2
                if( height == 1 ):
                    print("Hail stopped at height 1")
            elif( height != 1 ):
                height *= 3; height += 1
            print("Hail is currently at height " + str(height) )
main()
