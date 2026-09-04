import random

def main():
    name = input("Hello! What is your name?:")
    print(f"well",{name},"I am thinking of a number between 1 and 100.Take a guess.")
    number = random.randint(1,100)
    guess = 0

    while guess != number:
        guess = int(input("Take a guess."))
        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")

    print(f"Good job",{name},"You guessed my number!")

    #este tambien ya esta bien 



if __name__=="__main__":
    main()
