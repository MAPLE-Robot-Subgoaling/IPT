def main():
    hailHeight= int(input("Please enter the starting height of the hailstone:"))
    while (hailHeight != 1):
        if ((hailHeight % 2)== 0):
            currentHeight = hailHeight/2
            print("Hail is currently at height" ,currentHeight)
            hailHeight = currentHeight
        else: 
            currentHeight = (hailHeight * 3) + 1
            print("Hail is currently at height" ,currentHeight)
            hailHeight = currentHeight
    print("Hail stopped at height 1")
main()
