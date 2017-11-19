def main():
    temp = int(input("Please enter a temperature: "))
    scale = str(input("Please enter a 'C' for Celsius, or a 'K' for Kelvin: "))
    if scale == "C":
        if temp > 100:
            print("At this temperature, water is a gas")
        if temp >= 0 and temp <= 100:
            print("At this temperature, water is a liquid")
        if temp < 0:
            print("At this temperature, water is a solid")
    if scale == "K":
        if temp > 373.15:
            print ("At this temperature, water is a gas")
        if temp >= 273.15 and temp<= 373.15:
            print ("At this temperature, water is a liquid")
        if temp < 273.15:
            print("At this temperature, water is a solid")
main()
