
def main():


    height = 0 
    height = int(input("Please enter the starting height of the hailstone: "))
    
    while height != 1:
        mod = height % 2

        if mod == 0:
            mod = height // 2
            print("Hail is currently at height", mod)
            height = mod
            
        elif mod == 1:
            mod = height * 3 + 1
            print("Hail is currently at height", mod)
            height = mod
    else:
        print("Hail stopped at height", height)

main()
