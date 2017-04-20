




BOIL_CELSIUS = 100
FREEZE_CELSIUS = 0
BOIL_KELVIN = 373.15
FREEZE_KELVIN = 273.15

def main():
    userTemp  = float(input("What temperature is it?"" ")) 
    tempType = str(input("Is that number in Kelvin or Celsius?"" "))
    if(userTemp < FREEZE_CELSIUS and tempType == "C"):
        print("You have a solid")
    elif(FREEZE_CELSIUS < userTemp < BOIL_CELSIUS and tempType == "C"):
        print("You have a liquid")
    elif(userTemp > BOIL_CELSIUS and tempType == "C" ):
        print("You have a gas")
    elif(userTemp < FREEZE_KELVIN and tempType == "K"):
        print("you have a solid")
    elif(FREEZE_KELVIN < userTemp < BOIL_KELVIN and tempType == "K"):
        print("you have a liquid ")
    elif(userTemp > BOIL_KELVIN and tempType == "K"):
        print("you have a gas")
    
main()
