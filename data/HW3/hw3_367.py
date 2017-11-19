def main():
    tempUser = float(input("Please enter the temperature: "))
    scaleUser = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(scaleUser == 'K'):
        tempUser = (tempUser - 273.15)
    if(tempUser <= 0.0):
        print("At this temperature, water is a (frozen) solid.")
    elif(tempUser >= 100.0):
        print("At this temperature, water is a gas.")
    elif(tempUser > 0.0 and tempUser < 100.0):
        print("At this temperature, water is a liquid.")
main()
