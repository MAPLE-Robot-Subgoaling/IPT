def main():
    temp = 0.0
    which = ""
    temp = float(input("What is the value of the temperature?"))
    which = input("Is this in Celcius or Kelvin? (C/K)")
    cels = "C"
    kelv = "K"
    if which == cels:
        if temp <= 0:
            print("At this temperature, water is a solid.")
        if (temp > 0) and (temp < 100):
            print("At this temperature, water is a liquid.")
        if temp >= 100:
            print("At this temperature, water is a gas.")
    if which == kelv:
        if temp <= 273.2:
            print("At this temperature, water is a solid.")
        if (temp > 273.2) and (temp < 373.2):
            print("At this temperature, water is a liquid.")
        if temp >= 373.2:
            print("At this temperature, water is a gas.")
main()
