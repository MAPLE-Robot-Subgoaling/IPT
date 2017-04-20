
def main():

    startheight = int(input("Please enter the starting height of the hailstone: "))

    print("Hail is currently at height", startheight)
    while startheight > 1:
        if startheight % 2 == 0:
            startheight = startheight // 2
            print("Hail is currently at height" , startheight)
        elif startheight % 2 == 1:
            startheight = (startheight * 3) + 1
            print("Hail is currently at height" , startheight)

    if startheight == 1:
        print("Hail stopped at height", startheight)

main()
