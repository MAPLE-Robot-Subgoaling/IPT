 
def main():
    SOLID_WATERC = 0
    GAS_WATERC = 100
    SOLID_WATERK = SOLID_WATERC + 273.15
    GAS_WATERK = GAS_WATERC + 273.15
 
    temp = float(input("Please enter the Temperature: "))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if unit == "C":

        if unit == "C" and temp >= GAS_WATERC :
           print("At this Temperature,Water is Gaseous(gas)")
        
        elif unit == "C" and temp <= SOLID_WATERC :
            print("At this Temperature,Water is Solid(Frozen)")
        else : 
            print("At this Temperature,Water is Liquid")


    if unit == "K" :

        if  unit == "K" and temp >= GAS_WATERK :
            print("At this Temperature, Water is Gaseous(gas)")
        elif unit  == "K" and temp <= SOLID_WATERK :
            print("At this Temperature, Water is solid(Frozen)")
        else : 
            print("At this Temperature, Water is Liquid")
 
            
main()
