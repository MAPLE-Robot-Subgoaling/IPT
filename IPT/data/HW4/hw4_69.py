
def main():

    hail = int(input("Please enter the starting height for the hailstone: "))
    while hail > 1:
        print("Hail is currently at height", hail)
        if hail%2 == 0:
            hail = hail/2
        else:
            hail = (hail*3) + 1  
    print("Hail stopped at height", hail)

main()
