
def main():

    x = int(input("Please enter the width of the box: "))
    y = int(input("Please enter the height of the box: "))
    a = str(input("Please enter a symbol for the box outline: "))
    b = str(input("Please enter a symbol for the box fill: "))
    
    for n in range(0, y):
        c = ""
        for m in range(0, x):
            if n == 0 or n == (y - 1):
                c = c + a
            else:
                if m == 0 or m == (x - 1):
                    c = c + a
                else:
                    c = c + b
        print(c)

main()
