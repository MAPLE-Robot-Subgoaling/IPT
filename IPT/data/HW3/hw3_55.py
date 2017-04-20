def main():
    scale = str(input("What scale would you like to use? Celsius or Kelvin? "))
    temp = float(input("What is the temp of the water? "))
    if scale == "Celsius":
        if temp <= 0:
            print("At this temperature,  water is a solid.")
        if temp > 0 and temp < 100:
            print("At this temperature, water is liquid")
        if temp > 100:
            print("At this temperature, water is a gas.")
    if scale == "Kelvin":
        if temp <= 0:
            print("This is not possible.")
        if temp > 0 and temp < 273.15:
            print("At this temperature, water is solid.")
        if temp > 273.15 and temp < 373.15:
            print("At this temperature, water is liquid.")
        if temp > 373.15:
            print("At this temperature, water is a gas.")

main()
