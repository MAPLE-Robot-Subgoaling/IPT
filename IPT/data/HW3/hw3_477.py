

def main():
    
    Temp = float(input("Enter the temperature:  "))
    Type = input("Enter 'C' for Celsius, or 'K' for Kelvin: ")


    if Temp <= 273.15 and Type == "K" or Temp <= 0 and Type == "C":
        print("At this temperature, water is a solid.")

    elif Temp >= 373.15 and Type == "K" or Temp >= 100 and Type == "C": 
        print("At this temperature, water is a gas.")

    else:
        print("At this temperature, water is a liquid.")

main()
