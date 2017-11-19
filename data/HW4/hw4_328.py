def main():
    heightOfHailStone = int(input(" Please enter the height of hailstone :" ))
    while heightOfHailStone < 0 :
        print("Please enter a positive integer ")
        heightOfHailStone = int(input(" Please enter the height of hailstone :" ))
    while heightOfHailStone != 1:
        print("Hail is currently at height",heightOfHailStone)
        if heightOfHailStone % 2 == 0 :
            heightOfHailStone = heightOfHailStone // 2
        elif heightOfHailStone % 2 != 0 :
            heightOfHailStone = (heightOfHailStone * 3) + 1
    if heightOfHailStone == 1 :
        print("height of hailstone stopped at 1 ")
main()
