
def main():
    hailHeight=int(input("What is the current height of the hail? "))
    while hailHeight!=1:
        if hailHeight%2==0:
            hailHeight=hailHeight//2
            print("The height of the hail is ",hailHeight)
        elif hailHeight%2==1:
            hailHeight=hailHeight*3+1
            print("The height of the hail is ",hailHeight)
        else:
            print("This is a mathematical impossibility")
    print("The hail stopped at height 1")
main()
