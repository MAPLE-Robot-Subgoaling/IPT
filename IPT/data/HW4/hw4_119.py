def main():
    endHeight = 1
    height = int(input("Please enter the starting height of the hailstone: "))
    while height!= endHeight:
        print("Hail is currently at height "+str(height))
        if height%2==0:
            height = height//2
        else:
            height = height*3+1
    print("Hail stopped at height "+str(height))
main()
