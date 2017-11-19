def main():
    var_int = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", var_int)
    while var_int != 1:
        if var_int % 2 == 0:
            var_int = var_int // 2
            if var_int != 1:
                print("Hail is currently at height", var_int)
        else:
            var_int = (var_int * 3) + 1
            if var_int != 1:
                print("Hail is currently at height", var_int)
    print("Hail has stopped at height 1.")
main()
