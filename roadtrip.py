def main():
    answer = "" # 1. Initialize
    followup = ""

    while answer != "Yes!": # 2. condition hasta que diga yes se cumple la variable
        answer = input("Are we there yet?").strip().title() #3. update
        if answer == "Yes":
            followup = input("really?").strip().title()
        if followup == "Yes!":
            break


    print("we just arrived")



if __name__=="__main__":
    main()
