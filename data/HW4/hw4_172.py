def main():
    height = int(input("Please enter the starting height of the hailstone (positive integer greater than '1'): "))
    print("Hail is currently at height", height)
    while height < 1:
        if height < 1:
            print("Height must be a positive integer greater than 1")
        height = int(input("Please enter the starting height of the hailstone (positive integer greater than '1'): ")) 
    while height != 1:
        if height % 2 == 1:
            height = ((height * 3) + 1)
            print("Hail is currently at height", height)
        else:
            height = (height / 2)
            print("Hail is currently at height", height)
    print("Hail stopped at height", height)
main()
