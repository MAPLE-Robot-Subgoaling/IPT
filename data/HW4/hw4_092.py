def main():
    hailH=int(input("Please enter the starting height of the hailstone:"))
    while hailH != 1:
        print("The hailstone is currently at the height:", hailH)
        hailHMod=hailH%2
        if hailHMod == 1:
            hailH=hailH*3+1
        elif hailHMod == 0:
            hailH=hailH/2
    print("The hailstone stopped at height 1")
main()
