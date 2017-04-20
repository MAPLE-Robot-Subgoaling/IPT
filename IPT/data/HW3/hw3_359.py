

def main():
    temp = float(input("What is the numerical temperature?: "))
    celOrKel = str(input("Enter a C if it is in Celsius, or a K if it is in Kelvin. "))
    celOrKel = celOrKel.lower()
    if (temp <= 0):
        print("At this temperature, water is frozen solid. Also, if this was actually Kelvin, call NASA or something!")
    elif ( 0 < temp and temp < 373):
        if ( 0 < temp and temp < 100 and celOrKel == "c"):
            print("At this temperature, water is a liquid.")
        elif ( 100 < temp and celOrKel == "c"):
            print("At this temperature, water is a gas.")
        elif ( 0 < temp and temp <= 273 and celOrKel == "k"):
            print("At this temperature, water is frozen solid.")
        elif ( 273 < temp and temp < 373 and celOrKel == "k"):
            print("At this temperature, water is a liquid.")
    else:
        print("At this temperature, water is a gas.")

main() 
