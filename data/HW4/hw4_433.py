def main():
    height = int(input("Please enter the Starting height of the hailstone: "))
    while height != 1 :
        print("Hail is currently at height",height)
        if height % 2 == 0 :
           height = height // 2
        elif height % 2 == 1 :
            height = (3*height)+1 
    if height == 1 :
        print("Hail stopped at height 1")
main()
