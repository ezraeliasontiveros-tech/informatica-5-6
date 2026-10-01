def main():
    print("Welcome to the Times Table Quiz")
    while True:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10) "))
            if 1 <= times_table <= 10:


        except ValueError:
                print("enter a number")

        try:
            max_value = int(input("Enter the maximum value for your times table:"))
        except ValueError:
                    print("enter a number")







        if 1 <= times_table <= 10:

            print(f"Here is the {times_table} times table")


            for x in range(1, max_value+1):

                answer = x * times_table
                print(f"{x} times {times_table}?")
                user_answer = int(input("Answer:"))
                if user_answer == answer:
                    print("correct")
                elif user_answer != answer:
                    print("incorrect")

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
