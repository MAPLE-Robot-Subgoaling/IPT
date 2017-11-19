def main():
    temperature = float(input("Please enter a temperature: "))
    scale = input("Enter 'C' for Celcius or 'K' for Kelvin: ")
    if(scale == "K"):
        temperature -= 273.15
    if(temperature < 0):
        print("At this temperature, water is a solid")
    elif(temperature < 100):
        print("At this temperature, water is a liquid")
    else:
        print("At this temperature, water is a gas")
main()
