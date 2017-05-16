
def main():

    hailHeight = int(input("What is the starting height of the hailstorm? "))
    while hailHeight > 1:
        if hailHeight % 2 == 0:
            hailHeight = hailHeight/2
            print("Hail is currently at height", hailHeight)
        elif hailHeight % 2 == 1:
            hailHeight = (hailHeight * 3) + 1
            print("Hail is currently at height", hailHeight)

    print("Hail has stopped at height 1")
main()
