
def main():
    temp = float(input("please input the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C" and temp >= 100:
       print("At this temperature, water is a gas")
    if scale == "C" and temp <= 0:
       print("At this temperature, water is a (frozen) solid")
    if scale == "C" and temp > 0 and temp < 100:
       print("At this temperature, water is a liquid") 
    if scale == "K" and temp >= 373:
       print("At this temperature, water is a gas")
    if scale == "K" and temp <= 273:
       print("At this temperature, water is a (frozen) solid")
    if scale == "K" and temp > 273 and temp < 373:
       print("At this temperature, water is a liquid")
main()
