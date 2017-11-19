def main():
    heightHailstone = int(input("Please enter a positive integer for the he\
ight  "))
    while heightHailstone>1:
        if (heightHailstone%2==0):
            heightHailstone = heightHailstone/2
            print ("Hail is currectly at height" ,heightHailstone)
            if (heightHailstone ==1):
                print("Hail stopped at height", heightHailstone)     
        else:
            heightHailstone = heightHailstone*3 +1
            print("Hail is currently at height" ,heightHailstone)
main()
