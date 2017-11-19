def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        if height % 2 == 1 and height != 1:
            print("Hail is currectly at height:", height)
            height = height * 3 + 1
        elif height % 2 == 0 and height != 1:
            print("Hail is currently at height:", height)
            height = height // 2           
    print("Hail stopped at height: 1")
main() 
