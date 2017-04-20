
def main():
    END_HEIGHT = 1
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != END_HEIGHT:
        print("Hail is currently at height ", height)
        if height % 2 == 0: #evens
            height //= 2
        else: #odds
            height = height*3 + 1
    print("Hail stopped at height ", END_HEIGHT)
main()
