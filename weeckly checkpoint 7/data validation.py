def main():
    not_validated = True
    while not_validated:
        try:## para que el programa sin romperse

            number = int(input("Enter a number between 1 and 10:"))
            if number >=1 and number <=10:
                print("Number stored successfully.")
                not_validated = False # - break
            else:
                print("Enter a NUMBER.")
        except ValueError:
                print("Enter a NUMBER.")
    # while True:
    #     try:
    #         name = input("Enter your name:")
    #         f_letter = name[0]
    #         print("Name stored successfully.")
    #         break

    #     except IndexError:
    #         print("A name is required.")
    name = ""
    while name =="":
        name =input("enter your name:")
        if name =="":
            print("A name is required.")
        else:
            print("name stored successfully.")




if __name__=="__main__":
    main()
