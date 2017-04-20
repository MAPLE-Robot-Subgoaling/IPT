
def main():

    hail = int(input("Please enter the starting height of the hailstorm: "))
    print("Hail is currently at height", hail)

    while(hail != 1):
        if(hail % 2 == 0):
            print("Hail is currently at height", hail//2)
            hail = hail // 2
        else:
            print("Hail is curretnly at height", (hail * 3 + 1))
            hail = hail * 3 + 1
    print("Hail stopped at height 1")

main()
