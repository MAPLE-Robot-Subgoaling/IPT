
def main():
    hailHeight = int(input("What is the hailstone's current height as a positive integer? "))
    while(hailHeight > 1):
        print("Hail is currently at height", hailHeight)
        if(hailHeight == int(hailHeight/2)*2):
            hailHeight = int(hailHeight/2)
        else:
            hailHeight = hailHeight*3 + 1
    print("Hail stopped at height", hailHeight)
main()
