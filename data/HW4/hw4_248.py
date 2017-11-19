def main():
    GROUND = 1
    height = int(input("What height does the hailstone start at?: "))
    while height > GROUND:
        print("The stone is at height:", height)
        if height % 2 == 0:
            height = int(height / 2)
        elif height % 2 == 1:
            height = int((height * 3) + 1)
    print("The stone is at height:", height)
    print("The Hailstone hit the ground!")
main()
