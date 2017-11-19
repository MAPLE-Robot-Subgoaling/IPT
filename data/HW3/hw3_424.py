def main():
    temp = float(input("Please enter tempuature"))
    degrees = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))
    if temp >= 100 and degrees == 'C':
        print(" At this tempurature, water is a gas.")
    elif temp <= 0 and degrees == 'C':
        print(" At this tempurature, water is a solid")
    elif (temp < 100 and temp > 0) and degrees == 'C':
        print(" At this tempurature, water is a liquid")
    elif temp >= 373.2 and degrees == 'K':
        print("At this tempurature, water is a gas")
    elif ( temp < 373.2 and temp > 273.2) and degrees == 'K':
        print("At this tempurature, water is a liquid")
    elif temp <= 273.2 and degrees == 'K':
        print("At this tempurature, water is a solid")
    else:
        print("Invalid data")
main()
