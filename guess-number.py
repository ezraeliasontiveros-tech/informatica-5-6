import random

def main():
    name = input("hello! What is your name?:")
    print(f"well,{name},I am thinking of a number between 1 and 100. Take a guess.") #por que usamos variable y texto en el mismo print
    number = random.randint(1,10)
    guess = 0


    while guess != number:
        guess = int(input("take a guess:"))
        if  number > guess:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")

    print(f"good job,{name}! you guessed my number!")








if __name__=="__main__":
    main()
