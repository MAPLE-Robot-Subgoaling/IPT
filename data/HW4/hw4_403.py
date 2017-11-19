def main():
    hail = int(input("Please enter the height of the hailstone: "))
    while hail != 1:
        if hail % 2 == 0:
            hail = (hail // 2)
            print ("Hail stopped at height of", hail)
        else:
            hail = (hail*3) + 1
            print ("Hail stopped at height of", hail)
    print ("Hail stopped at height of 1")
main()
