


def main():
    hailStone=int(input("Please enter the starting height of the hailstones: "))
    HAIL_EXIT=1
    if(hailStone<HAIL_EXIT):
        while((hailStone<HAIL_EXIT)):
            hailStone=int(input("Please enter a starting hailstone height greater than '0': "))
    while(hailStone!=HAIL_EXIT):
        while((hailStone%2==0) and (hailStone!=HAIL_EXIT)):
            hailStone=(hailStone/2)
            print("Hail is currently at height: ",int(hailStone))
        while((hailStone%2!=0) and (hailStone!=HAIL_EXIT)):
            hailStone=((hailStone*3)+1)
            print("Hail is currently at height: ",int(hailStone))
    







main()
