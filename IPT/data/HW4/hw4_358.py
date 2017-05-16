
def main():
    num = int(input("Please enter the starting height of the hailstone: "))    

    while num != 1:
        if(num % 2 == 0):
            num = num / 2
        else:
            num = (num * 3) + 1

        print("The hail is currently at height:", num)

    print("The hail stopped at height:", num)

main()
