
def main():
    startheight = int(input("Enter the starting height of the hailstorm:"))
    while startheight < 0:
        startheight = int(input("Enter the starting height of the hailstorm:"))

    while startheight > 1:
            if (startheight % 2) == 0:
                startheight = startheight / 2
                print("Hail is currently at height", startheight)
            else: 
                startheight = (startheight * 3) + 1
                print("Hail is currently at height", startheight)

    print("Hail stopped at height 1")
main()
