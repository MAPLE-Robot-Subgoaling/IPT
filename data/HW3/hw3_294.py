def main () :
    tempScale = input("Please enter 'C' for Celcius or 'K' for Kelvin:")
    if tempScale == "K":
        waterTemp = float(input("Please enter the temperature:"))
        if waterTemp >= 373.15:
            print ("At this temperature, water is a gas.")
        elif waterTemp <= 273.15:
            print ("At this temperature, water is a solid.")
        else:
            print ("At this temperature, water is a liquid.")
    else:
        waterTemp = float(input("Please enter the temperature:"))
        if waterTemp >= 100:
            print ("At this temperature, water is a gas.")
        elif waterTemp <= 0:
            print ("At this temperature, water is a solid.") 
        else:
            print ("At this temperature, water is a liquid.")
main ()    
