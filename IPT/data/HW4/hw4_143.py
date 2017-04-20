
def main():
    height = input("Please enter the starting height of the hailstone: ")
    
    while height != "1":
        print("Hail is currently at height", height)
        if (height[-1] == "0") or (height[-1] == "2") or (height[-1] == "4") or (height[-1] == "6") or (height[-1] == "8"):
            height = int(height)
            height = height // 2
            height = str(height)
        elif (height[-1] == "1") or (height[-1] == "3") or (height[-1] == "5") or (height[-1] == "7") or (height[-1] == "9"):
            height = int(height)
            height = (height * 3) + 1
            height = str(height)
    print("Hail stopped at height", height)

main()
