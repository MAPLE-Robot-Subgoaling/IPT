def main():
    height = int(input("Please enter a positive integer: "))
    if height == 1:
        print("Hail current height is", height)
    else:
        while height != 1:
            if height == 1:
                print("Hail current height is", height)
            elif height % 2 == 0:
                height = height // 2
                print("Hail current height is", height)
            elif height % 2 == 1:
                height = (height * 3) + 1
                print("Hail current height is", height)
main()
