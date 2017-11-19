def main():
    status = ("Hail is currently at height ")
    Height = int(input("Please enter the starting height of the hailstone: "))
    print(status +str(Height))
    while(Height != 1):
        while(Height % 2 == 0) and Height != 1:
            Height = Height // 2
            if(Height != 1):
                print(status +str(Height))
        while(Height % 2 == 1) and Height != 1:
            Height = (Height*3) + 1
            print(status +str(Height))
        if(Height == 1):
            print("Hail stopped at height 1")
            quit()
main()
