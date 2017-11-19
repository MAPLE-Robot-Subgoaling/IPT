def main():
    height = int( input("Please enter the starting  height of the hailstorne"))
    if height == 1:
        print("exit the program")
        exit()
    while height > 1:
        if height % 2 == 0:
            height = height / 2
            print("hailstone is :", height) 
        else:
            height = (height * 3) + 1
            print("hailstone is: ", height)
main()
