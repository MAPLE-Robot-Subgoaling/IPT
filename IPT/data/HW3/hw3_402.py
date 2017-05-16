
def main():

    temp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if(tempType == "K" or tempType == "k"):
        if(temp >= 373.16):
            print("At this temperature, water is a gas.")
        elif(temp <= 273.16):
            if(temp < 0):
                print("This is not a valid temperature, Absolute Zero is 0 degrees Kelvin.")
            else:
                print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    elif(tempType == "C" or tempType == "c"):
        if(temp >= 100):
            print("At this temperature, water is a gas.")
        elif(temp <= 0):
            if(temp < -273.16):
                print("This is not a valid temperature, Absolute Zero is -273.16 degrees Celsius.")
            else:
                print("At this temperature, water is a (frozen) solid.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        print("You entered an invalid temperature scale.")

main()
