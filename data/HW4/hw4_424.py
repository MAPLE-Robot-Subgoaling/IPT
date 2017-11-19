def main():
    height = int(input("Enter the height of hailstone"))
    while height != 1 :
        if height % 2 == 0:
            height = (height // 2)
            print("The height of hailstone is", height)
        else:
            height = ((height*3)+1)
            print("the height of hailstone is", height) 
    print("Hailstone stopped at height 1")
main()
