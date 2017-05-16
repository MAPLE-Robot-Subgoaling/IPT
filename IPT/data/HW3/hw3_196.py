
def main():

    temp = float(input("WHAT IS TEMP"))
    if (input("SHELSHIUS OR KELVIN CLEIN") == "K"):
        if (temp >= 375.15):
            print("very gassy")
        elif (temp <= 273.15):
            print("very solid")
        else:
            print("very liquidy")
    else:
        if(temp >= 100):
            print("very gassy")
        elif (temp <= 0):
            print("very solid")
        else:
            print("very liquidy")
main()
