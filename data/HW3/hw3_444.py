def main():
    temp = float(input("Enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if tempScale == "C":
        if temp <= 0 :
            print("The water will be frozen solid at this temperature.")
        elif 0 < temp < 100 :
            print("The water is a liquid at this temperature.")
        elif temp >= 100 :
            print("At this temperature the water is a gas.")
    else:
        if temp <= 273.15 :
            print("The water will be frozen solid at this temperature.")
        elif 273.15 < temp < 373.15 :
            print("The water is a liquid at this temperature.")
        elif temp >= 373.15 :
            print("At this temperature the water is a gas.")
main()
