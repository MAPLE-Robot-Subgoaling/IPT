temp = float(input("Please enter the temperature: "))
SI = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
if SI == 'C' and temp > 100:
    print("At this temperature, water is gas. ")
elif SI == 'C' and temp > 0:
    print("At this temperature, water is liquid")
elif SI == 'C' and temp <= 0:
    print("At this temperature, water is ice")
elif SI == 'K' and temp > 373.15:
    print("At this temperature, water is gas")
elif SI == 'K' and temp > 273.15:
    print("At this temperature, water is liquid")
else:
    print("At this temperature, water is ice")
