def main():
    w = int(input("Enter the width of the rectangle:"))
    print("O"*w)
    print("O"*w)
    print("O"*w)
    print("O"*w)
    print("O"*w)

    p =(5*2) + (w*2)
    print("Perimeter:",p)

    a =(5*w)
    print("area:",a)


    d =((5**2)+(w**2)**0.5)
    print("Diagonal:",d)





if __name__=="__main__":
    main()
