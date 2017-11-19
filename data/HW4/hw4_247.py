num = int(input("What height is the hail at? "))
print("Hail is currently at height ",int(num))
if (num == 1):
    quit()
while(num != 1):
    if(num % 2 == 0):
       num /= 2
       print ("Hail is currently at height ",int(num))
    else:
        num *= 3
        num += 1
        print("Hail is currently at height ",int(num))
