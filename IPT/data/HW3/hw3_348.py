
def main():
    
    temp = input("Pleas enter the temprature: ")
    temp = float(temp)
    measure  = input("pleas enter 'c' for Celsius, or 'k' for Kelvin: ")
   
    if ((temp <= 0 and measure =="c")or (temp <= 273.5 and measure == "k")):
        print("At this temprature, Water is a (frozen) solid.")
    elif ((temp >= 100 and measure =="c")or (temp >= 373.5 and measure =="k")):
        print("At this temprature, water is a gas.")
    else:
        print("At this temprature, water is a liquid.")
main()
