def main():
    posInt = int(input("Please enter a starting positive integer for height of the hailstone: "))
    while (posInt != 1):
        if (posInt % 2 == 0) and (posInt - 2 != 0):
            posInt = posInt // 2
            print("Hail is currently at height", posInt)
        elif ((posInt % 2 == 1) and (posInt != 1)):
            posInt = posInt * 3 + 1
            print("Hail is currently at height", posInt)
        else:
            posInt = posInt // 2
    print ("Hail stopped at height 1")
                 
main()
