
def main():
    enterTemp = float(input("Please enter the temperature: "))
    typeTemp = input("Please enter 'C' for Celsisus, or 'K' for Kelvin: ")


    if typeTemp == "K" and enterTemp >= 373.16:
        print("At this temperature, water is a gas.")
    elif typeTemp == "K" and enterTemp <= 273.16:
        print("At this temperature, water is a solid.")
    elif typeTemp == "K" and (enterTemp < 373.16 and enterTemp > 273.16):
        print("At this temperature, water is a liquid.")
    elif typeTemp == "C" and enterTemp >= 100:
        print("At this temperature, water is a gas.")
    elif typeTemp == "C" and enterTemp <= 0:
        print("At this temperature, water is a solid.")
    else: 
        print("At this temperature, water is a liquid.")
                                 
                                                                      

main()
