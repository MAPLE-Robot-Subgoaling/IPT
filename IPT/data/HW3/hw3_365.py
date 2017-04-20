



def main():


    
    waterTemperature = float(input("Please enter the temperature:"))
    
    temperatureScale = input("Please enter 'C' for Celsius or 'K' for Kelvin:")


    if waterTemperature < 0 and temperatureScale == "C":
       print("At this temperature, water is solid.")

    if waterTemperature < 273.15 and temperatureScale == "K":
       print ("At this temperature, water is solid.")
    

    elif  waterTemperature < 100 and waterTemperature > 0  and temperatureScale == "C":
       print("At this temperature, water is liquid.")  

    elif  273.15 < waterTemperature < 375.15 and temperatureScale == "K":
       print(" At this temperatue, water is liquid:.")

    else: print(" At this temperature, water is gas")



main()
