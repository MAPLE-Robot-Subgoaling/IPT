
def main():

    temp = float(input("What is the temperature in degrees? "))
    scale = input("What is the scale: Celsius (C) or Kelvin (K)? ")
    
    if scale == "C":
        if temp <= 0:
            print("At this temperature, water is a solid.")
        elif (temp > 0) and (temp < 100):
            print("At this temperature, water is a liquid.")
        elif temp >= 100:
            print("At this temperature, water is a gas.")

    if scale == "K":
        if temp <= 273.16:
            print("At this temperature, water is a solid.")
        if (temp > 273.16) and (temp < 373.16):
            print("At this temperature, water is a liquid.")
        if temp >= 373.16:
            print("At this temperature, water is a gas.")

main()
