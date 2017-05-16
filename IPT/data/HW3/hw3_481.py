
def main():
     
    temp = float(input("Please enter the temperature:"))
    units =input("Please enter 'C' for Celsius, or 'K' for Kelvin:")

    if units == "K"  and temp >= 373:
        print("At this temperature, water is a gas")
    if units== "K" and ( temp < 373 and  temp > 273):
        print("At this temperature is a liquid")
    if units == "K" and temp <= 273:
        print("At this temperature water is a solid")
    if units == "C" and temp >= 100:
        print("At this temperature water is a gas")
    if units == "C" and (temp < 100 or temp > 0):
        print("At this temperature water is a liquid")
    if  units == "C" and temp < 0 :
        print("At this temperature water is a solid")

main()
