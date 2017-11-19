def main():
    hailStone = int(input("Please enter the starting height of the hailstone: "))
    while hailStone != 1:
        if hailStone % 2 == 1:
            hailStone = (hailStone*3) + 1
            print("Hail is currently at height", hailStone)
        elif hailStone % 2 == 0:
            hailStone = hailStone // 2
            print("Hail is currently at height", hailStone)
    print("Hail is stopped at height", hailStone)
main()    
