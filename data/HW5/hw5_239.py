def main():
     width = int(input ("Please enter the width of the box: "))
     hight = int(input ("Please enter the height of the box: "))
     outSimple =(input ("Please enter a symbol for the box outline: "))
     innSimple =(input (" Please enter a symbol for the box fill: "))
     for i in range(hight):
         for a in range(width):
             if ( i == 0 or i == (hight-1) or a==0 or a ==(width-1)):
                 print( outSimple,end='')
             else:
                 print(innSimple,end='')
         print()
main()
