EVEN = 2
def main():
    height = int(input("What is the initial height of the hailstone? "))
    while (height > 1):
        if ((height/EVEN) == int(height/EVEN)):
            height = int(height/2)
        else:
            height = height*3
            height = int(height + 1)
        print("Hail is currently at height ", height)
main()
