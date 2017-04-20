
def main():

    END = 1
    hail = int(input("Enter the starting height of the hailstorm: "))

    while hail != END:
        if hail % 2 == 0:
            hail = hail // 2
            print("The height is currently", hail)
        elif hail % 2 == 1:
            hail = hail * 3 + 1
            print("The height is currently", hail)

    print("The hail stopped at height", hail)
                
main()
