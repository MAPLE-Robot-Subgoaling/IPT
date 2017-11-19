def main():
    divide = 2
    add = 1
    multiply = 3
    ground = 1
    height = int(input("Please enter the starting height of the hailstone: "))
    while(height > ground):
        while(height % 2 != 1):
            print("Hail is currently at height" , height)
            height = int(height / divide)
        while(height % 2 == 1 and height != ground):
            print("Hail is currently at height" , height)
            height = int((height * multiply) + add)
    print("Hail stopped at height" , height)
main()
