def main():

    tasks = []

    while True:
        print(f"You have {len(tasks)} to do.")
        print(tasks)
        command = input("what do you want to do? (add,complete, or close):").lower()
        if command == "add":
            new_task = input("Enter a task:")
            tasks.append(new_task)
        if command == "complete":
            com = input("what task is completed:")
            tasks.remove(new_task)
            print(com)

        elif command == "close":
            break





if __name__=="__main__":
    main()
