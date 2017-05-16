
def main():
    heightHail = int(input("Please enter the starting height of the hailstone: "))
    
    while (heightHail != 1):
        if (heightHail % 2 == 0):
            print("The hail is currently at height", int(heightHail))
            heightHail = (heightHail / 2)
        elif (heightHail % 2 != 0):
            print("The hail is currently at height", int(heightHail))
            heightHail = ((heightHail * 3) + 1)
    
    print("Hail stopped at height", int(heightHail))

main()
