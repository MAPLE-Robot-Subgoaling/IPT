def main():
    heightHail = input("Please enter the starting height of the hailstone: ")
    heightHail = int(heightHail)
    while(heightHail != 1):
        if(heightHail % 2 == 0):
            heightHail=heightHail/2
            print("Hail is currently at height", heightHail)
        elif(heightHail % 2 == 1):
            heightHail=heightHail*3 + 1
            print("Hail is currently at height", heightHail)
    print("Hail is stopped at height", heightHail)
main()
