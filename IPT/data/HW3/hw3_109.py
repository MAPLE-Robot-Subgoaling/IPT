
def main():
     temp = float(input("Pleas enter the temperature:"))
     scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
     if scale == "C":
       if temp <= 0:
           print("At this temperature, water is a(frozen) solid.")
       elif temp >= 100:
            print("At this temperature, water is a gas.")
       elif temp > 0 and tem < 100:
            print("At this temperature, water is a liquid.")
     elif scale == "K":
       if temp <= 273.15 and temp >= 0:
            print("At this temperature, water is a(frozen) solid.")
       elif temp >= 373.15:
            print("At this temperature, water is a gas.")
       elif temp > 273.15 and tem < 373.15:
            print("At this temperature, water is a liquid.")
       elif temp < 0:
            print("You cannot have a temperature below 0 Kelvin,it is the abosulte zero.But you can think this as a solid.")
     elif scale != "C" or "K":
            print("The answer you type in is invalid, make sure you type in capitalized 'C'or 'K'.")
main()
