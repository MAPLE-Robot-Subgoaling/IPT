
def main():

    temp = float(input("Please enter a number"))
    value = input("Please enter a 'C' for celsius, or 'K' for Kevlin")

    if value.upper() == "C":
        if temp <= 0:
            print(" At this temperture, water is solid(ice/frozen)")
        elif temp < 100 and temp > 0:
            print(" At this temperture, water is a liquid.")
        elif temp >= 100:
            print(" At this temperture, water is a gas.")
    
    elif value.upper() ==  "K":
        if temp >= 373.16:
            print(" At this temperature, water is a gas.")
        elif temp <= 273.16:
            print(" At this temperature, water is solid(frozen)")



main()
