

def main():

    length = int(input("Please enter the  length of the box. "))
    width = int(input("Please enter the width of the box. "))
    edge = str(input("Please enter what the border of the box should be. "))
    fill = str(input("Please enter what the fller of the box should be. "))
    outer = edge * length
    inner = edge + (fill* (length-2)) + edge 
    for i in range(1):
        print(outer)
    if length != 1:    
        for j in range(width - 2):
            print(inner)
    if length == 1:
        for k in range(width - 2):
            print(edge) 
    
    if width != 1:
        for h in range(1):
            print(outer)

main()
