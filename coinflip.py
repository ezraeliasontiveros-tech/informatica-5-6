import random

def main():
    coin = random.randint(1,2)
    guess = int(input("guess on the coin flip game:"))

    # sides = ["heads","tails"]

    if coin == 1:
        print("heads")

    elif coin == 2:
        print("tails")


    if guess == coin:
        print("you win")
    elif guess != coin:
        print("you lose")












if __name__=="__main__":
    main()
