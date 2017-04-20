
def main():
    
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "K":
        temp = temp - 273.15
        
    if temp > 100:
        state = "gas"
    elif temp < 0:
        state = "solid"
    else:
        state = "liquid"

    print("At this temperature, water is a",state)       

main()
