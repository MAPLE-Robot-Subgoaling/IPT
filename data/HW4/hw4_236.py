def main():
    height=int(input("Please enter the starting height of the hailstone:"))
    while height>1:
        if height%2==0:
           height= height//2
           print("Hail is currently at",height)
        else:
            height= (height*3)+1
            print("Hail is currently at",height)
    print("Hail has stopped at height 1")
main()
