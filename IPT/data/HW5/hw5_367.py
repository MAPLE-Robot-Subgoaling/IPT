
def main () :
    boxWid = int(input("Please enter the width of the box: "))
    boxHeit = int(input("Please enter the height of the box: "))
    outSym = input("Please enter a symbol for the box outline: ")
    fillSym = input("Please enter a symbol for the box fill: ")
    topBot_list = [outSym]*boxHeit   # creates left border
    topBot_list[0] = outSym*boxWid   # creates top border
    topBot_list_len = (len(topBot_list)-1)  # initializes num for middle sections
    for listItem in range(1,topBot_list_len ):
        topBot_list[listItem ] = (outSym + ((boxWid-2)*fillSym)) + outSym
    
    topBot_list[boxHeit-1] = outSym*boxWid   # creates bottom border
    
    for N in topBot_list:
        print(N)



main ()
