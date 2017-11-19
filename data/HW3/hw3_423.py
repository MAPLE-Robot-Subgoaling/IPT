def maine():
   t = int(input("Please enter the tempurature:"))
   l = str(input("Please enter 'c' for Celsius, or 'k' for Kelvin:"))
   if t <= 0 and l == "c":
       print ("At this tempurature, water is a solid (frozen)")
   if t <273 and l == "k":
       print ("At this tempurature, water is a solid (frozen)")
   if t > 0 and t <100 and l =="c":
       print (" At this tempurature, water is a liquid")
   if t>= 273 and t <373 and l == "k":
       print (" At this tempurature, water is a liquid")
   if t > 100 and l == "c":
       print ("At this tempureture, water is a gas")
   if t >= 373 and l == "k":
       print ("At this tempureture, water is a gas")
maine()
