
def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "K":
        tempC = temp - 273.15
    else:
        tempC = temp

    if tempC <= 0:
        print("At this temperature, the water is a solid.")
    elif tempC >  0 and tempC < 100:
        print("At this temperature, the water is a liquid.")
    elif tempC >= 100:
        print("At this temperature, the water is a gas.")

main() 
