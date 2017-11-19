def main():
    userTemp = float(input("Please enter the temperature: "))
    userSystem = input("Please enter 'K' for Kelvin or 'C' for Celsius: ")
    if userSystem == "C":
        if userTemp < 0:
            print("At this temperature, water is frozen solid.")
        if userTemp > 0 and userTemp < 100:
            print("At this temperature, water is in a liquid state.")
        if userTemp > 100:
            print("At this temperature, water in in a gaseous state.")
        if userTemp == 0:
            print("This is the temperatura at which water changes states bewteen solid and liguid. The two should be able to exist at equilibrium.")
        if userTemp == 100:
            print("This is the temperatura at which water changes states bewteen liguid and gas. The two should be able to exist at equilibrium.")
    if userSystem == "K":
        if userTemp < 273.15:
            print("At this temperature, water is frozen solid.")
        if userTemp > 273.15 and userTemp < 373.15:
            print("At this temperature, water is in a liquid state.")
        if userTemp > 373.15:
            print("At this temperature, water in in a gaseous state.")
        if userTemp == 273.15:
            print("This is the temperatura at which water changes states bewteen solid and liguid. The two should be able to exist at equilibrium.")
        if userTemp == 373.15:
            print("This is the temperatura at which water changes states bewteen liguid and gas. The two should be able to exist at equilibrium.")
main()
