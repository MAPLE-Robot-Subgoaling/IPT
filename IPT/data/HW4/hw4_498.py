
def main():

    END_HEIGHT = 1

    height = input("Please give me a positive integer: ")
    height = int(height)

    print("Hail is currently at height ", height)


    while height > END_HEIGHT:
        evenOdd = height % 2

        if evenOdd == 0:
            height = height / 2
            print("Hail is currently at height ", height)

        else:
            height = (height * 3) + 1
            print("Hail is currently at height ", height)
    print("Hail stopped at height ", 1)

main()
