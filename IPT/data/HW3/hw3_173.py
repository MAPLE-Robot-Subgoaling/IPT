
def main():

    temperature = float(input("What is the temperature? "))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin. ").upper()

    if(unit == "K"):
        temperature -= 273
    
    if(temperature >= 100):
        print("At this temperature, water is a gas.")

    elif(temperature > 0):
        print("At this temperature, water is a liquid.")

    else:
        print("At this temperature, water is a solid.")

main()
