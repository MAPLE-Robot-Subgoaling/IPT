def main ():
    hailHeight = int(input(" Please enter the starting height of the hailstone:  "))
    hailStop = 1
    HEIGHT_EVEN = 0
    HEIGHT_ODD = 1
    print ("Hail is currently at height",hailHeight)
    while hailHeight > hailStop:
        if hailHeight % 2 == HEIGHT_EVEN and hailHeight != hailStop:
            hailHeight = int( hailHeight / 2
)
            if hailHeight == hailStop:
                print ("Hail stopped at height", hailHeight)
                exit
            else:
                print ("Hail is currently at height",hailHeight)
        elif hailHeight % 2 == HEIGHT_ODD:
            hailHeight = hailHeight * 3 + 1
            if hailHeight == hailStop:
                print ("Hail stopped at height", hailHeight)
                exit
            else:
                print ("Hail is currently at height",hailHeight)
main()
