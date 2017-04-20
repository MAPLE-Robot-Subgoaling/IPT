
def main():

    num = int(input("gib hight pls C: "))
    
    print("hale is height high: " + str(num))
    
    while num != 1:
        
        if num%2 == 0:
            num = num//2
            print("hale is height at: " + str(num))
        else:
            num = (num*3)+1
            print("hale hight at is: " + str(num))

    print("height turned into juan")

main()
