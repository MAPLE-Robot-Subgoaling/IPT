
def main():

    height = int(input("Please choose a positive integer: "))
    while (height > 1):
        if (height % 2 == 0):
            height = int(height / 2)
            print("Height is currently at height", height)
        elif (height % 2 == 1):
            height = int((height * 3) + 1)
            print("Hail is currently at height", height)
    print("Hail stopped at height 1.")
               
main()
