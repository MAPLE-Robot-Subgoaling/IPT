

def main():
    num = int(input("Please enter the starting height of the hailstone: "))
    while num > 1:
        if num % 2 ==0:  #even
           num = int(num - (num/2))
           print("Hail is currently at height: " + str(num))
        else:     #odd 
           num = int((num *3) + 1)
           print("Hail is currently at height: " + str(num))
    print("Hail has stopped at height 1 ")

main()
