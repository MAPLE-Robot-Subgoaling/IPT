def main():
    temp = float(input("Please enter the temperature: "))
    cOrK = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    cOrK.upper()
    if(cOrK == 'C'):
        if(temp <= 0):
            print("At this temperature, water is a solid.")
        elif(temp < 100):
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    elif(cOrK == 'K'):
        if(temp <= 273):
            print("At this temperature, water is a solid.")
        elif(temp < 373):
            print("At this temperature, water is a liquid.") 
        else:
            print("At this temperature, water is a gas.")
main()
