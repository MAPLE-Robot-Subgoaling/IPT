def main():
    height = int(input("Please enter the starting height of the hailstorm:"))
    heightF = int( height/2)
    print("Hail is currently at height", heightF)
    while heightF > 2:
        if heightF%2 == 0 :
            heightF = int(heightF/2)
            print("Hail is currently at height:",heightF)
        elif heightF%2 == 1:
            heightF = int((heightF*3)+1)
            print("Hail is currently at height:",heightF)
    if heightF == 2:
        print("Hail stopped at height 1")
main()
