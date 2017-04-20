

def main():


    starting_Height=int(input("Please enter the starting height of the hailstone:"))
    while  starting_Height !=  1:
         if starting_Height%2 == 0:
           new_Height = starting_Height//2
           print("Hail is currently at height", new_Height)
           starting_Height = new_Height
         else:
           new_Height = starting_Height * 3 + 1
           print("Hail is currrently at height", new_Height)
           starting_Height = new_Height

    print("Hail stopped at height 1")               
                   
main()
