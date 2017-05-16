
height = int(input("Please enter the height of the box: "))
width = int(input("Please enter the width of the box: "))
perimeter = str(input("Please enter a symbol to be used for the perimeter of the box: "))
area = str(input("Please enter a symbol to be used for the inside of the box: "))

list1 = [perimeter] * width
list2 = [area] * width
list2[0] = perimeter
list2[-1] = perimeter
print (''.join(list1))
for i in range(0,height-2):
    print (''.join(list2))
print (''.join(list1))
