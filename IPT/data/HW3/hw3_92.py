def main():
      temp= float(input("please enter the temperature:"))
      scale=input("please enter 'C' for Celsius or'K' for Kelvin:")
      if (temp==0) and (scale=="C"):
         print("At this temperature water is a (frozen) solid.")
      elif (temp==100) and (scale=="C"):
         print ("At this temperature water is gas.")
      elif (temp<100) and (temp>0) and (scale=="C"):
         print("At this temperature water is liquid.")
      elif (temp==273) and (scale=="K"):
          print("At this temperature water is freez.")
      elif (temp==373) and (scale=="K"):
          print("At this temperature water is gas.")
      elif (temp<373)and (temp>273)and (scale=="K"):
          print("At this temperature water is liquid.")
main()
