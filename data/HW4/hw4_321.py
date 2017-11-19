def main():
    print("It's time to follow a hailstone through a storm.")
    STOP_HEIGHT = 1
    height = int(input("How high does it start up? >"))
    while height > STOP_HEIGHT:
        print("The hailstone is at height", height)
        if height % 2 == 0:
            height = height // 2
        elif height % 2 > 0:
            height = (height * 3) + 1
    print("Hail stopped at height", height)
main()
