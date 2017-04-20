
temp = float(input("What is the temperature?"))

scale = input("What is the scale(c or k)?")

if scale == "c":
    if temp <= 0:
        print("At this temperature, water is a solid.")
    elif temp > 0 and temp < 100:
        print("At this temperature, water is a liquid.")
    else:
        print("At this temperature, water is a gas.")
else:
    if temp <= 273.15:
        print("At this temperature, water is a solid.")
    elif temp > 273.15 and temp < 373.15:
        print("At this temperature, water is a liquid.")
    else:
        print("At this temperature, water is a gas.")
