flavorText = "Hail is currently at height"
def main():
    height = 0 
    while height < 1:
        height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        print(flavorText, height)
        if (height % 2) == 0:
            height //= 2
        else:
            height = (height * 3) + 1
    print("Hail stopped at height", height)
main()
