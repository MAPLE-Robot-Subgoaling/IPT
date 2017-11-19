def main():
    units = input("what are the units of tempature? (k/c)")
    temp = (float)(input("what is the tempature of the water?"))
    if units == "k":
        if temp >= 373.16:
            print("boiling")
        elif temp <= 273.16:
            print("frozen") 
        else : 
            print("water")
    elif units == "c":
        if temp >= 100:
            print("boiling")
        elif temp <= 0:
            print("frozen") 
        else : 
            print("water")
main()
