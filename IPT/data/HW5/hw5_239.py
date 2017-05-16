def main():
    width=int(input("Enter the width please "))
    height=int(input("Enter the height please "))
    symbolO=raw_input("Enter the outline character please ")
    symbolF=raw_input("Enter the fill character please ")
    widthN=width-2
    heightN=height-2
    if widthN>0:
        lineO=[symbolO]
        lineM=[symbolO]
        for i in range(1,widthN):
            lineO.append(symbolO)
            lineM.append(symbolF)
        lineO.append(symbolO)
        lineM.append(symbolO)
    elif widthN==0:
        lineO=[symbolO,symbolO]
        lineM=[symbolO,symbolO]
    else:
        lineO=[symbolO]
        lineM=[symbolO]
    if heightN>0:
        print(lineO)
        for i in range(heightN):
            print(lineM)
        print(lineO)
    elif height==0:
        print(lineO)
        print(lineO)
    else:
        print(lineO)
main()
