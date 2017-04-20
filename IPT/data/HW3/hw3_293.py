
def main():
    temp=float(input("Please enter the temperature:"))
    unit=input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if unit == "C" and temp > 100.0:
        print("At this temperatiure, water is Gas")
    elif unit == "C" and temp < 0:
        print("At this temperature, you should go out and experience the freeze. BTW water is a solid")
    elif unit == "K" and temp < 273:
            print("At this temperature, water will freeze")
    elif unit == "K" and temp > 373:
            print("At this temperature, water will be gas")
    else:
            print("Water is normal as you usually see")
main()
