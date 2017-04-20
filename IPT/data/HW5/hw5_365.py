




def main():


    width = int(input("Please enter the width of the box:"))
    height= int(input("Please enter the height of the box:"))
    
       
  
    outline_symbol = input("Please enter a symbol for the box outline:")
    box_fill_symbol= input("Please enter a symbol for the box fill:")



    print(outline_symbol* width)
  
    for i in range(height-2):
      print(outline_symbol + box_fill_symbol*(width-2) + outline_symbol)
    
    if height > 1:
      print (outline_symbol* width)   
    
        
main()
