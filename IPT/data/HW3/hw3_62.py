
def main():
    Temperature = float(input("Please enter the tempreature"))
    KelvinandCelsius = input("please enter the kelvin or celsius")
    if KelvinandCelsius =="celsius":
        if Temperature >= 100:
            print(" Water is boiling")
        elif Temperature <=0:
            print("Water is frozen")
        else: 
            print("Water is liquid")    
    if KelvinandCelsius =="kelvin":
        if Temperature >=373.16:
            print("Water is boiling")
        elif Temperature <=2733.16:
            print("Water is boiling")
        else:
            print("Water is liquid")
main()
