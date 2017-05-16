
EVEN_OP= 2
ODD_OP1= 3
ODD_OP2= 1
def main():

    strHeight= int(input("Please enter the starting height of the hailstone: "))
    evenOddChck= strHeight % 2
    print("Hail is currently at",strHeight)
    while strHeight > 1:
        while evenOddChck == 0 and strHeight != 1:
            strHeight= strHeight // EVEN_OP
            print("Hail is currently at",strHeight)
            evenOddChck= strHeight % 2
        while evenOddChck != 0 and strHeight != 1:
            strHeight= (strHeight * ODD_OP1) + ODD_OP2
            print("Hail is currently at",strHeight)
            evenOddChck= strHeight % 2

    print("Hail stopped at height 1.")

main()
