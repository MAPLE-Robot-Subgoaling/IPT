def main():
    height = int(input("Enter height"))
    while height != 1:
        print("Hail currently at height", height)
        if height % 2 == 0:
            height = height // 2
        else:
            height = height * 3 + 1
    print("Hail stopped at height", height)
main()
