def main():
    fruits = ["apple","banana","cherry"]
    print("pineapple" not in fruits) ## IN es para ver si un elemento es parte de una lista

    tasks =[]

    while True:
        print(f"tasks to do:{len(tasks)}")
        print(tasks)

        new_task = input("enter task:").capitalize().strip()

        if new_task =="Exit":
            break

        if new_task not in tasks:
            tasks.append(new_task)
        elif new_task in tasks:
            del_confirm = input("did you completed{new_task}?(y/n):").lower().strip()
            if del_confirm == "y":
                tasks.remove(new_task)
            else:
                continue






if __name__=="__main__":
    main()
