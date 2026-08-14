def main():
    # planet = input("Planet:")

    # #separation
    # print("hello", planet)

    # #ending
    # print("hello",end=" ")
    # print(planet)

    # # concatenation
    # print("hello " +planet)

    # #formatted string
    # print(f"hello {planet}")

    name = input("what´s your name?").title().strip()
    color = input("tell me a color:").lower().strip()
    adj = input("give me an adjetive:").lower().strip()
    goal = input("a goal would like to achive:").lower().strip()

    print(f"hello {name}!")
    print()

    print("this is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.")


    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.".upper())




if __name__=="__main__":
    main()




