FREEZING_POINT_OF_CELSIUS= 0
BOILING_POINT_OF_CELSIUS = 100
FREEZING_POINT_KELVIN = 373.16
BOILING_POINT_KELVIN= 273.16
def main():
    temp= float(input("Please enter the temperature:"))
    temp1= (input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))
    if temp1 =="C":
        if temp > 0 and temp < 100:
            print("At this temperature, water is a liquid.")
        elif temp <=100:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a gas.")
    else:
        if temp > 273.16 and temp < 373.16:
            print("At this temperature, water is a liquid.")
        elif temp <= 273.16:
            print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a gas.")
main()
