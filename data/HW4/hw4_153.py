def main():
    height = int(input("What is the height of the hailstone?"))
    while  height != 1:
        if height % 2 == 0:
             print("The height of the hailstone is currently:",height) 
             height = height // 2
        elif height % 2 != 0:
            print("The height of the hailstone is currently:",height) 
            height = (height*3)+1
    print("The height of the hailstone is currently: 1")
main()
