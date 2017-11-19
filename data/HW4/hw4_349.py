def main():
    alt = int(input("please enter the starting height of the hailstone: "))
    while alt != 1:
        if alt % 2 == 1:
            alt = ((alt * 3 + 1)*2)//2
            print("Its height is", alt) 
        elif alt % 2 == 0:
            alt = alt // 2
            print("Its height is", alt)
main()
