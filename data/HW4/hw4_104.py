def main():
    print() 
    print("Welcome to hailstone simulator!") 
    print("The storm outside is howling.") 
    heightHailstone = int(input("How high do you want to drop your hailstone? ")) 
    print() 
    while heightHailstone != 1: 
        if (heightHailstone % 2) == 0: 
            heightHailstone = int(heightHailstone / 2)
        elif (heightHailstone % 2) == 1: 
            heightHailstone = int((heightHailstone * 3) + 1)
        print("Hail is currently at height", heightHailstone) 
    print("Hailstone has landed.") 
    print() 
main()
