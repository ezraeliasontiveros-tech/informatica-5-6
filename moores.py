def main():
    transistors = 17.8
    years = int(input("Number of years:"))
    current_year = 2026

    if(current_year + years) >=2030:
        print("The law is not valid.")
    else:
        transistors *= 2**(years/2)

        print(transistors, "Billons")







if __name__=="__main__":
    main()
