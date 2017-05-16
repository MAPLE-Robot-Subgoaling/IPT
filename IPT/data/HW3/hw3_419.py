
temp = float(input("Please enter the temperature: "))
CorK = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

if(CorK == "C"): 
    if(temp > 100): print("At this temperature, water is a gas.")
    elif(temp < 0): print("At this temperature, water is a solid.")
    else: print("At this temperature, water is a liquid.")
if(CorK == "K"):
    if(temp > 373.15): print("At this temperature, water is a gas.")
    elif(temp < 273.15): print("At this temperature, water is a solid.")
    else: print("At this temperature, water is a liquid.")
