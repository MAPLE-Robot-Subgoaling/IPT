def main():
    num=int(input("Please enter a positive number"))
    while num!=1 and num>0:
        if num%2==0:
            num=num/2
            print("Hailstone Height Is",num)
        else:
            num=(num*3)+1
            print("Hailstone Height Is",num)
    print("Hailstone has stopped at",num)        
main()
