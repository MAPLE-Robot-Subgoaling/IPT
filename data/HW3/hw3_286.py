def main():
    temp = float(input("Please enter the temperature: "))
    celorfah = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    if temp >= 100 and celorfah == "C":
       print("At this temperature, water is a gas.")
    elif temp <= 0 and celorfah == "C":
       print("At this temperature, water is (frozen) solid.")
    elif temp >= 1 and temp <= 99 and celorfah == "C":
       print("At this temperature, water is a liquid.")
    elif temp >= 373 and celorfah == "K":
        print("At this temperature, water is a gas.")
    elif temp <= 273 and celorfah == "K":
       print("At this temperature, water is a (frozen) solid.")
    elif temp >=91  and temp <=372 and celorfah == "K": 
        print("At this temperature, water is a liquid.")
main()
