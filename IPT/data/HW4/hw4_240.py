
def main():

    heightStone = int(input("Please enter the height of the hailstone"))

    while heightStone != 1:
        if heightStone % 2 == 0:
            heightStone = heightStone / 2
            print(heightStone)

        else:
            heightStone = (3 * heightStone) + 1
            print(heightStone)

main()
