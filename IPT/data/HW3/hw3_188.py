
def main():

    temp = int(input("Please enter the temperature:"))
    kc = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin:"))

    if kc=="C":
        if temp <= 0:
            print("At this temperature, water is a solid")
        elif temp >= 100:
            print("At this temperature, water is a gas") 
        else :
            print("At this temperature, water is a liquid")
    elif kc=="K":
        if temp <= 273.16:
            print("At this temperature, water is a solid")
        elif temp >= 373.16:
            print("At this temperature, water is a gas")
    else :
        print("At this temperature, water is a liquid")

main()





