def main():
    def highest(a,b):
        if a>b:
            highest_num = a
        elif b>a:
            highest_num = b
        elif a = b:
            print("both are the highest")
        print(f"The highest number entered is {highest_num}")
    num1 = int(input("Enter a number:"))
    num2 = int(input("enter another number:"))

    highest(num1,num2)

    def lowest(a,b,c):
        if a<b and a<c:
            lowest_num = a
        elif b<a and b<c:
            lowest_num = b
        elif c<a and c<b:
            lowest_num = c
        else
            print("Try another number")
        print(f"the lowest number entered is {lowest_num}")

    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    num3 = int(input("Enter another number:"))
    lowest(num1,num2,num3)





if __name__=="__main__":
    main()
