

def main():

    temperatureWater = float(input("Please enter the water temperature.  ",))

    scaleMeasure = str(input("If the water temperatue in Celsius, please enter C or temperature in Kelvin, Please enter K.  ",))



    if( temperatureWater <= 273.15 and scaleMeasure == "K") or (temperatureWater <= 0 and scaleMeasure == "C"):

        print("The water is in solid(frozen) when the temperature is", temperatureWater ,scaleMeasure )

    elif (temperatureWater >= 373.15 and scaleMeasure == "K") or  (temperatureWater >= 100 and scaleMeasure == "C"):
  
      print("The water is gas when  the temperature is", temperatureWater ,scaleMeasure )

    else:

        print("The water is in liquid when  the temperature is" ,temperatureWater, scaleMeasure)

main()
