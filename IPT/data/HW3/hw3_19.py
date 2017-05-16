

def main():
    print("Welcome to the water state questionaire!")
    print("This program tells you the state of water based on user input.")
    theTemp=float(input("Enter a temperature: "))
    kelvinCelsius=str(input("Please enter C for Celsius and K for Kelvin."))
    if (kelvinCelsius == "K"):
        actualTemp=theTemp-273.15
    else:
        actualTemp=theTemp
    if (actualTemp<=0):
        print("At this temperature, the water is in a solid state.")
    elif (actualTemp > 0 and actualTemp < 100):
        print("At this temperature, the water is in a liquid state.")
    else:
        print("At this temperature, the water is in a gas state.")
main()

    
        
    
    
                 
