def main():
    temp = float(input("Please enter the temperature: "))
    temp_scale = str(input("Please enter 'C' for Celcius, or 'K' for Kelvin: "))
    state=""
    if temp_scale == "C":
                        if temp <= 0:
                         state="(frozen) solid."
                        elif temp>0 and temp<100:
                         state="liquid."
                        else:
                         state="gas."
    if temp_scale == "K":
                        if temp<=273.16:
                         state="(frozen) solid."
                        if temp>273.16 and temp<373.16:
                         state="liquid."
                        if temp>=373.16:
                         state="gas."
    print("At this temperature, water is a", state)
main()
