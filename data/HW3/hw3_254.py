def main():
    Temp = float(input("Please enter a tempreture : "))
    CK = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if CK == 'C':
        if Temp >= -273 and Temp <= 0:
            print("At this temperature, water is solid ")
        if Temp > 0 and Temp <= 100:
            print("At this temperature, water is liquid ")
        if Temp > 100:
            print("At this temperature, water is gas ")
    elif CK == 'K':
        if Temp >= 0 and Temp <= 273:
            print("At this temperature, water is solid ")
        if Temp > 273 and Temp <= 373:
            print("At this temperature, water is liquid ")
        if Temp > 373:
            print("At this temperature, water is gas ")        
main()
