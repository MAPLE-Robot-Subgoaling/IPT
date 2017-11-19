def main():
    hailHite = int(input(
            "Please enter the starting height of the hailstone "))
    while hailHite != 1:
        if hailHite % 2 == 1:
            hailHite = (hailHite * 3) + 1
            print ("Hail is currently at a height of", 
                   (hailHite), "meters")
        else:
            hailHite = hailHite // 2
            print ("Hail is currently at a height of", 
                   hailHite, "meters")
    print("Hail stopped at height 1")
main()
