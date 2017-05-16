
def main():

    scaleType = input("What temperature scale would you like? Please enter 'K' for kelvins or 'C' for Celcius. ")
    if scaleType == "C":
        tempC = float(input("What is the temperature of the water? "))
        if tempC <= 0.0:
            print("At this temperature, water is solid ice.")
        if tempC > 0.0:
            print("At this temperature, water is a liquid.")
        if tempC > 100.0:
            print("At the temperature, water is gaseous water vapor.")
    if scaleType == "K":
        tempK = float(input("What is the temperature of the water? "))
        if tempK <= 0:
            print("That's impossible!")
        if tempK > 0:
            print("At this temperature, water is solid ice.")
        if tempK > 273.2:
            print("At this temperature, water is a liquid.")
        if tempK > 373.2:
            print("At this temperature, water is gaseous water vapor.")

main()
