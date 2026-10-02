def main():
    print("Welcome to the Times Table Quiz")

    while True:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10) "))
            if 1 <= times_table <= 10:
                while True:
                    try:
                        max_value = int(input("Enter the maximum value for your times table:"))
                        if 1 <= max_value <= 10:
                            break
                    except ValueError:
                        print("enter a number")


                print(f"Here is the {times_table} times table")


                for x in range(1, max_value+1):

                    answer = x * times_table
                    print(f"{x} times {times_table}?")
                    while True:
                        try:
                            user_answer = int(input("Answer:"))
                            break
                        except ValueError:
                            print("enter a number")
                    if user_answer == answer:
                        print("correct")
                    elif user_answer != answer:
                        print("incorrect")

                    else:
                        print("Invalid command.")



        except ValueError:
            print("enter a number")


if __name__ == "__main__":
    main()
