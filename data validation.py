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


if __name__=="__main__":
    main()
