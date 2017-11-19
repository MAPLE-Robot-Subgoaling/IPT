def main():
    temperatureScale = input("Enter C for tempeartures measured with Celsius and K for temperatures measured with Kelvins: ")
    temperatureNumber = float(input("Please enter your measured number here: "))
    if(temperatureScale == "C"):
        if(temperatureNumber <= 0):
            print("At this temperature water is a solid.")
        elif(temperatureNumber > 0 and temperatureNumber <100):
            print("At this temperature water is a liquid.")
        elif(temperatureNumber >= 100):
            print("At this temperature water is a gas.")
    elif(temperatureScale == "K"):
        if(temperatureNumber <= 273.15):
            print("At this temperature water is a solid.")
        elif(temperatureNumber > 273.15 and temperatureNumber < 373.15):
            print("At this temperature water is a liquid.")
        elif(temperatureNumber >= 373.15):
            print("At this temperature water is a gas.")
main()
