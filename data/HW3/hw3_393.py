temp=input("Please enter the temperature: ")
unit=input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
if unit=="C":
               if unit<"0":
                   print("At this temperature, water is a (frozen) solid.")
                   if unit>"0" and unit<"100":
                       print("At this temperature, water is a liquid")
                       if unit>"100":
                           print("At this temperature, was is a gas")
if unit=="K":
               if unit<"273":
                   print("At this temperature, water is a (frozen) solid.")
                   if unit>"273" and unit<"373":
                       print("At this temperature, water is a liquid")
                       if unit>"373":
                           print("At this temperature, was is a gas")
