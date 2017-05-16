
END = 1

def main():
    erraticHail = int(input("Please enter the starting height of the hailstone: "))

    while erraticHail < END:
        print("Invalid height. Please check the height again.")
        erraticHail = int(input("Enter the starting height: "))

    print ("The erratic hailstone starts out at height", erraticHail)

    while erraticHail != END:
        if (erraticHail // 2) == (erraticHail / 2):
            erraticHail = erraticHail // 2
            print("The erratic hailstone height is currently", erraticHail)
        else:
            erraticHail = erraticHail * 3 + 1
            print("The erratic hailstone height is currently", erraticHail)

    print ("Hailstone stopped at height", END)
            
main()
