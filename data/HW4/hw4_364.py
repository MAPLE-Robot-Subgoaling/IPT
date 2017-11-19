def main():
    height = int(input("Please enter the starting height of the hailstone: ")) 
    STOP_HEIGHT = 1 
    FALLING_DIVIDER = 2 
    BOUNCE_MULTIPLIER = 3 
    BOUNCE_CONSTANT = 1 
    while True:
        height = height // FALLING_DIVIDER if not height % 2 else height * BOUNCE_MULTIPLIER + BOUNCE_CONSTANT
        if height != STOP_HEIGHT:
            print("Hail is currently at height %s" % height)
        else:
            break
    print("Hail stopped at height %s" % STOP_HEIGHT)
main()