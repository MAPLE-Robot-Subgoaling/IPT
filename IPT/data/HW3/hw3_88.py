
def main():
 measurement = str(input("Is the temperature in celsius or kelvin (C or K)"))

 if measurement == "K":    
    temperatureK = float(input("Please enter the temperature"))
    if temperatureK > 372.2:
                            print("The water is a gas")
    elif temperatureK < 273.2:
                            print("The water is a solid")
    else:
                            print("The water is a liquid")

 elif measurement == "C":
    temperatureC = float(input("Please enter the temperature"))
    if temperatureC > 100:
                            print("The water is a gas")
    elif temperatureC < 0:
                            print("The water is a solid")
    else:
                            print("The water is a gas")

                            
 main()
