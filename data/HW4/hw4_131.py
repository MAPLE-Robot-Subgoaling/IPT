def main():
    height = str(input("What is the height of the hailstone? "))
    while height != "1":
        height = str(height)
        if height[-1] == "0" or "2" or "4" or "6" or "8":
            height = int(height)
            height = height/2
            height = int(height)
            print("Hail is currently at height", height)
            height = str(height)
        elif height[-1] == "1" or "3" or "5" or "7" or "9" and height != "1":
            height = int(height)
            height = height * 3 + 1
            height = int(height)
            print("Hail is currently at height", height)
            height = str(height)
    else:
        print("Hail stopped at height 1")
main()
