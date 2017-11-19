def main():
    hailStone = int(input("Please enter the staring height of the hailstone: "))
    while hailStone != 1 :
        print("Hail is currently at height ", hailStone )
        if  (hailStone % 2) == 0:
            hailStone = hailStone/2
        elif (hailStone % 2) == 1:
            hailStone = (3 * hailStone) + 1
    print("Hail stopped at height ", hailStone)
main()
