def main():
    height_of_hailstone = int(input("Please enter the starting height of the hailstone: "))
    while height_of_hailstone != 1:
        print("Hail is currently at height",height_of_hailstone)
        if ( height_of_hailstone % 2 ) != 0:
            height_of_hailstone = int(( height_of_hailstone * 3 ) + 1 )
        elif ( height_of_hailstone % 2 ) == 0:            
            height_of_hailstone = ( height_of_hailstone // 2 )
    print("Hail stopped at height 1")
main()
