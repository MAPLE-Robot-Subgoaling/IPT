def main():
    SOLID_TEMP = 0
    GAS_TEMP = 100
    waterTemp = float(input("What is the temperature of water?:"))
    unitTemp = input("Please enter 'K' for Kelvin or 'C' for Celcius")
    if unitTemp == 'K' or unitTemp == 'k':
        waterTemp = waterTemp - 273
    if waterTemp <= 0:
        print("At this temperature, water is solid")
    elif waterTemp >= 100:
        print("At this temperature, water is gas")
    else: 
        print("At this temperature, water is liquid")
main()
