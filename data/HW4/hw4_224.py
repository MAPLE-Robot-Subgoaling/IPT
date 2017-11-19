def main():
    height = int(input("Please enter the current height of the hailstone: "))
    while height != 1:
        if height % 2 == 0:  
            newHeight = height // 2
            print("Hail is currently at height", height)
            height = newHeight
        elif height % 2 == 1:
            newHeight = (height * 3) + 1
            print("Hail is currently at height", height)
            height = newHeight
    if height == 1:
        print("Hail stopped at height 1")
main()
