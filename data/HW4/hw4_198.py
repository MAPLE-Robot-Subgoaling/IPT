def main():
    THREE = 3
    TWO  = 2
    ONE  = 1
    ZERO = 0
    hailHeight = int(input("Please enter a positive integer:  "))
    if hailHeight < ONE:
        print("You need to enter a positive integer")
        hailHeight = int(input("Please enter a positive integer:  "))
    if hailHeight > ONE:
        while hailHeight > ONE:
            if hailHeight % TWO == ZERO:
             hailHeight = hailHeight / TWO
             print(int(hailHeight))
            elif hailHeight % TWO == ONE:
                hailHeight = hailHeight * THREE + ONE
                print(int(hailHeight))
    print("The hailstorm has stoppped")
main()
