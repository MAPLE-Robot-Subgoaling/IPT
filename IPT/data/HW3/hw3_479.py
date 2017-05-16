
def main():

    temperature = float(input("Please enter the temperature: "))
    scaleOfTemperature = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")

    if scaleOfTemperature == "C":
        if temperature <= 0:
            print("At this temperature, Water is solid.")
        elif temperature >= 100:
            print("At this temperature, Water is gas.")
        else:
            print("At this temperature, Water is liquid.")

    elif scaleOfTemperature == "K":
        if temperature <= 273:
            print("At this temperature, Water is solid.")
        elif temperature >= 373:
            print("At this temperature, Water is gas.")
        else:
            print("At this temperature, Water is liquid.")

    else:
        print("Error: Check your input")



main()
