def main():
    temp=float(input("Please enter the temperature: "))
    scale=input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if temp <= 0 and scale == "C":
        print("At this temperature, water is a solid.")
    elif temp > 0 and temp < 100 and scale == "C":
        print("At this temperature, water is a liquid.")
    elif temp >= 100 and scale == "C":
        print("At this temperature, water is a gas.")
    if temp <= 273.16 and scale == "K":
        print("At this temperature, water is a solid")
    elif temp > 273.16 and temp < 373.16 and scale == "K":
        print("At this temperature, water is a liquid.")
    elif temp >= 373.16 and scale == "K":
        print("At this temperature, water is a gas.")
main()
