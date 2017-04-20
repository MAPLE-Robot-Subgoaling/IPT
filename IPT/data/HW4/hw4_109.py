
def main():
    currentnum = input("Please enter the starting height of the hailstone:")
    currentnum = int(currentnum)
    evenorodd = currentnum % 2
    while currentnum != 1:
        print("Hail is currently at height",currentnum)
        if evenorodd == 0:
            currentnum = (currentnum // 2)
        elif evenorodd == 1:
            currentnum = ((currentnum * 3) + 1) 
        evenorodd = currentnum % 2
    print("Hail stopped at height 1")
main()
