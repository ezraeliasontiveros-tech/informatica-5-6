import random

def main():
    coin = ["heads", "tails"]
    attempts = 3
    while attempts > 0: #es para que se repita mientras la condicion se cumpla
        flip = random.choice(coin)
        guess = input("heads or tails?").strip().lower()

        print("the coin landed on",flip)

        if guess == flip:
            print("tou won")
            break     #es para romper algo
        else:
            print("gg")
            attempts -= 1
            print("attempts left:",attempts)

    if attempts == 0:
        print("game over")






if __name__=="__main__":
    main()
