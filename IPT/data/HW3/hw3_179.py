      
def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")

    if scale == "C":
        if temp <= 0.0:
            print("At this temperature, water is a solid.")
        if 0 < temp < 100:
            print("At this temperature, water is a liquid.")
        if temp >=100:
            print("At this temperature, water is a gas.")
    
    elif scale == "K":
        if temp <= 273:
            print("At this temperature, water is a solid.")
        if 273 < temp < 373.15:
            print("At this temperature, water is a liquid")
        if temp >= 373.15:
            print("At this temperature, water is a gas.")

main()
