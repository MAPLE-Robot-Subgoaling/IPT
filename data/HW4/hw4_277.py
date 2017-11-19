def main():
    height = int(input("Please enter the starting height of the hailstone:"))
    while height!= 1:
        if height%2 == 0:
            print("Hail is currently at height", height/2,)
            height=(height/2)
        else:
            print("Hail is currently at height",height*3 + 1,)
            height=(height*3+1)
    print("Hail stopped at height 1")
main()
