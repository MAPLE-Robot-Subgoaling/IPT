def main():
    hailheight = float(input("please enter starting height of the hailstone: "))
    print("Hail is currently at height",hailheight)
    while hailheight > 1:
        if hailheight % 2 == 0:
            hailheight = hailheight / 2
            print("Hail is currently at height",hailheight)
        elif hailheight % 2 == 1:
            hailheight = hailheight * 3 + 1
            print("Hail is currentlly at height",hailheight)
    print("Hail stopped at height 1")
main()
