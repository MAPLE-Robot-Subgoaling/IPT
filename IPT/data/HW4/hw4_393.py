
def main():

    height = int(input("Please enter the starting height of the hailstone: "))

    while height !=1:
        if height % 2 ==0:
            height = height / 2
            print(height)
        else:
            height = (3 * height) +1
            print(height)

main()
