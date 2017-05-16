
temperature = int(input("please enter the temperature:"))
unit = input("please input 'C' for Celsius, or 'K' for Kelvin:")

if unit == "C" and temperature <= 0:
    print("At this temperature, water is solid.")
if unit == "C" and temperature < 100 and temperature > 0:
    print("At this temperature, water is a liquid.")
if unit == "C" and temperature > 100:
    print("At this temperature, water is a gas.")
if unit == "K" and temperature <= 273.15:
    print("At this temperature, water is solid.")
if unit == "K" and temperature < 373.15 and temperature > 272.15:
    print("At this temperature, water is a liquid.")
if unit == "K" and temperature > 373.15:
    print("At this temperature, water is a solid.")
