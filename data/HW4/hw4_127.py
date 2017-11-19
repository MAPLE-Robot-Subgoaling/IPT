def main():
    Height=int(input("Please enter the starting heoght of hailstone "))
    while Height!=1:
        while Height%2==0 and Height!=1:
            print("Hail is currntly at height ", Height)
            Height = int(Height/2)
            while Height%2!=0 and Height!=1:
                print("Hail is currently at height", Height)
                Height = (Height*3)+1
        while Height%2!=0 and Height!=1:
            print("Hail is currently at height ", Height)
            Height = (Height*3)+1
            while Height%2==0 and Height!=1:
                print("Hail is currently at height ", Height)
                Height = int(Height/2)
    print("Hail stopped at height", Height)
main()
