temp = float(input("Please enter the temperature: "))
unitOfTemp = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
def main():
    if(unitOfTemp == "C"):
        if(temp <= 0):
            print("At this temperature, water is a (frozen) solid.")
        elif(temp >= 100):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    elif(unitOfTemp == 'K'):
        if(temp <= 273.2):
            print("At this temperature, water is a (frozen) solid.")
        elif(temp >= 373.2):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
main()
