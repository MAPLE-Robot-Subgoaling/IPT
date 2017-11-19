def main():
    hieght = int(input("Please enter the initial hieght of the hailstone: "))
    print("Hailstone at:", hieght)
    while(hieght>1):
        if(hieght%2 == 0):
            hieght = hieght // 2
        elif(hieght%2 == 1):
            hieght = (hieght * 3) + 1
        print("Hailstone at:", hieght)
    print("Hailstone has stopped")
main()
