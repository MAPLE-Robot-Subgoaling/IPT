
def main():
    STOP_HEIGHT = 1
    
    height = int(input("Please enter the starting height of the hailstone: "))

    while height != 1:
        if height % 2 == 0:
            height = int(height / 2)
        else:
            height = int(3 * height + 1)

        print("Hail is currently at height", height)
            
    print("Hail stopped at height", height)

main()
