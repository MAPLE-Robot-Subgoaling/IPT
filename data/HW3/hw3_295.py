def main ():
    print ("Hello")
    userTemp = float(input("At what temperature would you like me to check water's state of matter?: "))
    tempUnit = input("Is this in 'F' Fahrenheit or 'C' Celsius. Please capitalize!?: ")
    print ()
    if tempUnit == "F":
        if userTemp >= 212:
            print ("Water is in it's gaseous state at ",userTemp," degrees Fahrenheit.")
        elif userTemp <= 32:
            print ("Water is in it's solid state at ",userTemp," degrees Fahrenheit.")
        else:
            print ("Water is in it's liquid state at ",userTemp," degrees Fahrenheit.")
    elif tempUnit == "C":
        if userTemp >= 100:
            print ("Water is in it's gaseous state at ",userTemp," degrees Celsius.")
        elif userTemp <= 0:
            print ("Water is in it's solid state at ",userTemp," degrees Celsius.")
        else:
            print ("Water is in it's liquid state at ",userTemp," degrees Clesius.")
main ()
