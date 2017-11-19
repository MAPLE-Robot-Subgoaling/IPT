def main():
    FINISH_HEIGHT = 1
    hailHeight = int(input("It's hailing men! What height is the hailstone? "))
    while (hailHeight < FINISH_HEIGHT):
        print("Sorry, men only fall from heights greater than 0.")
        hailHeight = int(input("What height is the hailstone? "))
    while (hailHeight != FINISH_HEIGHT):
        print("Hail is currently at ", hailHeight)
        if hailHeight % 2 == 0:
            hailHeight = hailHeight // 2
        else:
            hailHeight = hailHeight * 3 + 1
    print("Hail has stopped at 1. You got your man.")
main()
