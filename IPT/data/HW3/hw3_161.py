
def main():
    temperature = int(input("Please enter the temperature:"))
    COrK = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))

    if COrK == 'C' and temperature <= 0:
                     print("At this temperature, water is a (frozen) solid.")
    elif COrK == 'C' and temperature >= 100:
                     print("At this temperature, water is a gas.")
    elif COrK == 'C' and 0 < temperature > 100:
                     print("At this temperature, water is a liquid.")
    if COrK == 'K' and temperature <= 273: 
                     print("At this temperature, water is a (frozen) solid.")
    elif COrK == 'K' and temperature >= 373:
                     print("At this temperature, water is a gas.")
    elif COrK == 'K' and 273 < temperature < 373:
                     print("At this temperature, water is a liquid.")
        








main()
