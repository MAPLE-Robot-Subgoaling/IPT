def main():
    stone = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height ", stone)
    while stone > 1:
        if stone % 2 == 0:
            stone = stone / 2
        else:
            stone = (stone * 3) + 1
        if stone == 1:
            print("Hail stopped at height", int(stone))
        else:
            print("Hail is currently at height ", int(stone))
main()
