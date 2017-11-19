def main():
    ADDFORKELVIN = 273.13
    SUBFORCELIUS = 32
    Temperature = float(input("Please enter the temperature "))
    Kelvin = (Temperature +  ADDFORKELVIN)
    Celcius = (Temperature - SUBFORCELIUS)
    Scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin ")
    if Scale == "C":
        if Celcius <= 0:
            print("At this temperature, water is a (frozen) solid.")
        else:
            if 100 > Celcius > 0:
                print("At this temperature, water is a liquid.")
            else:
                if Celcius >= 100:
                    print("At this temperature, water is a gas")
    else:
        if Scale == "K":
            if Kelvin <= 273.15:
                print("At this temperature, water is a (frozen) solid.")
            else:
                if Kelvin >= 373.15:
                    print("At this temperature, water is a gas")
                else:
                    if 373.15 > Kelvin > 273.15:
                        print("At this temperature, water is a liquid")
main()
