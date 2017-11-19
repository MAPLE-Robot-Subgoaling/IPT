ZER = 273.15
def main():   
    temp = float(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempType == "C":
        if temp <= 0:
             print("At this temperature, water is a (frozen) solid.")
        elif temp >= 100:
             print("At this temperature, water is a gas.")
        else:
              print("At this temperature, water is a liquid.")
    else:
        temp = (temp - ZER)
        if temp <= 0:
             print("At this temperature, water is a (frozen) solid.")
        elif temp >= 100: 
             print("At this temperature, water is a gas.")
        else:
              print("At this temperature, water is a liquid.")
main()
