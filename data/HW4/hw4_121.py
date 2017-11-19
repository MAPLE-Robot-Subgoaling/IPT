def main():
    height = 0
    height = int(input("Enter the starting height of the hailstorm"))
    while( height != 1):
        if(height % 2 == 0):
            height = height / 2
            print("Height of the hailstorm is", height)
        else:
            height = 3*height+1
            print("Height of the hailstorm is", height)
main()
