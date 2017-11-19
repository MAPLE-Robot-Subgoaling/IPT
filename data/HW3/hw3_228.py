def main():
    temp = float(input("Please enter the temperature: "))
    measure = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if (temp <=  0 and measure == "C") or (temp <= 273 and measure == "K"):
        print("At this temperature, water is (frozen) solid.")
    elif (temp < 100 and measure == "C") or (temp < 373 and measure == "K"):
        print("At this temperature, water is liquid.")
    if(temp >= 100 and measure == "C") or (temp >= 373 and measure == "K"):
        print("At this temperatur, water is gas.")
main()
