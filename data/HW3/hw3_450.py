def main():
    KELVIN_IS_CELSIUS=273.15
    FROZEN=0
    GAS=100
    tempNum=float(input("Please enter the temperature: "))
    tempScale=input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(tempScale == "K"):tempNum = tempNum-KELVIN_IS_CELSIUS
    if(tempNum<=FROZEN):print("At this temperature, water is (frozen) solid.")
    if(tempNum>FROZEN and tempNum<GAS):print("At this temperature, water is liquid.")
    if(tempNum>=GAS):print("At this temperature, water is gas.")
main()
