
def main():
    temp = float(input("Please enter the temperature: "));
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ");
    if (scale == "K"):
        temp = (temp - 273.15);
    if (temp <= 0):
        state = ("(frozen) solid");
    if (temp >= 100):
        state = ("gas");
    if (temp < 100 and temp > 0):
        state = ("liquid")
    print("At this temperature, water is a", state);



main()
