
def main():

    hailHeight = int(input("Please enter the starting height of the hailstone: "))
    while hailHeight != 1:
        if (hailHeight % 2 == 0):
            hailHeight = hailHeight/2
        if (hailHeight % 2 != 0):
            hailHeight = hailHeight*3 + 1
        print("Hail is currently at height", hailHeight)

main()
