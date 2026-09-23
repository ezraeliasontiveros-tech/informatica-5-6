def main():
    number =[1,2,3,4,5,6,7,8,9,10]
    while number <=10 and number >0:
        print(f"Here is the{number} times table")
        for i in range(len(number)):
            print(f"1 times {number} is [i*{number}]")




if __name__=="__main__":
    main()
