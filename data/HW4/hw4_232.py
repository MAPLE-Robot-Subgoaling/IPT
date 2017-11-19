def main():
    hailNum = int(input("Please enter the starting height of the hailstone: "))
    while hailNum != 1 :
        print (" Hail is currently at height", int(hailNum) )
        if hailNum % 2 == 0: 
            hailNum = hailNum / 2
        elif hailNum % 2 != 0: 
            hailNum = (hailNum * 3) +1 
    print("Hail stopped at height 1")
main()
