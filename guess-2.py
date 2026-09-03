import random

def main():
    name = input("hello! What is your name?:")
    print(f"well",{name},"I am thinking of a number between 1 and 100. Take a guess.")

    number = random.randint(1,100)
    guess = 0

    while guess != number:
        guess = int(input("take a guess:"))
        if guess > number:
            print("your guess is too high.")
        elif guess < number:
            print("your guess is too low.")

    print(f"good job,{name}! you guessed my number!")

if __name__=="__main__":
    main()

    #este esta bien 
