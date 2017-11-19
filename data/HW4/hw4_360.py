def main():
    num = int(input("Please enter the starting height of the hailstone: ")) 
    while num != 1: 
        if (num % 2 == 1):
            num = (num * 3) + 1
            print("Hail is currently at height of", num)
        elif (num % 2 == 0):
            num = (num / 2)
            print("Hail is currently at height of", num)
    print("Hail stopped")
main()
