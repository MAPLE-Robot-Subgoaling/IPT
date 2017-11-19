def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        if height % 2 == 0 :
            height =  (height // 2)
            print(" The hail height is", height )
        else:
            height = ((height * 3)+1) 
            print(" The hail height is", height)
    print("Hail stopped at height 1")
main()
