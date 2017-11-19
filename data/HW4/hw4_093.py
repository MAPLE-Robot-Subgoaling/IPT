LOOP_CONTROL = 1
EVEN = 0
EVEN_II = 2
ODD = 1
DIVISOR = 2
MULTI = 3
ADD = 1
def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while(height != LOOP_CONTROL):
        print("Hail is currently at height", height)
        mod = int(height % DIVISOR)
        if(mod == EVEN or mod == EVEN_II):
            height = int(height / DIVISOR)
        elif(mod == ODD):
            height = int(height * MULTI + ADD)
    print("Hail stopped at height 1")
main()
