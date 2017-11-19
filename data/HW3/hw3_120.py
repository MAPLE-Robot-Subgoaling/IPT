def main ():
    temp = float(input("Please enter the temperature: "))
    tempScale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if (tempScale == "C") and (temp > 0) or(temp < 100):
        print("At this temperature, water is a liquid")
    elif (tempScale == 'C') and (temp <= 0):
        print("At this tempterature, water is a frozen solid")
    elif (tempScale == 'C') and (temp >= 100):
        print("At this tempterature, water is a gas")
    elif (tempScale == 'K') and (temp>273.15) or (temp < 373.15):
        print("At this temperature, water is a liquid")
    elif (tempScale == 'K') and (temp <= 273.15):
        print("At this temperature, water is frozen solid")
    else:
        print("At this tempterature, water is a gas")
main ()
