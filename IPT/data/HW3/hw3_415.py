
def main():

    temp = float(input("Please enter the temerature: "))

    typeDegree = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    cel = "C"
    
    CEL_ZERO = 0
    CEL_BOIL = 100

    kel = "K"

    KEL_ZERO = 273.16
    KEL_BOIL = 373.16

    if typeDegree == cel:

        if (temp  < CEL_ZERO):
            print("At this temperature, water is a solid")
        
        if (temp > CEL_ZERO and temp < CEL_BOIL):
            print("At this temperature, water is a liquid")

        if (temp > CEL_BOIL):
            print("At this temperature, water is a gas")

    if typeDegree == kel:

        if (temp < KEL_ZERO):
            print("At this temperature, water is a solid")

        if (temp > KEL_ZERO and temp < KEL_BOIL):
            print("At this temperature, water is a liguid")

        if (temp > KEL_BOIL):
            print("At this temperature, water is a gas")

main()

    
