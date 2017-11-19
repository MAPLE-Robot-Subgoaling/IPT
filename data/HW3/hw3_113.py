def main():
    temp = float(input("Please enter the temperature: "))
    measure = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if (100 > temp > 0 and measure == 'C'):
        print("At this temperature, water is liquid")
    elif (212 > temp > 32 and measure == 'K'):
        print("At this temperature, water is lquid")
    elif (temp <= 0 and measure == 'C'):
        print("At this temperature, water is frozen")
    elif (temp <= 32 and measure == 'K'):
        print("At this temperature, water is frozen")
    elif (temp >= 100 and measure == 'C'):
        print("At this temperature, water is gas")
    elif (temp >= 212 and measure == 'K'):
        print("At this temperature, water is gas")
main()
