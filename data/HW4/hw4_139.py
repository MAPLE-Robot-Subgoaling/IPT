def main():
    height = int(input("Please enter the starting height of the hail: "))
    while not(height == 1):
        print("Height of hail: " , height)
        if height % 2 == 0:
            height = height // 2
        else:
            height = (height * 3) + 1
    print("Hail stopped at height " , height , ".")
main()
