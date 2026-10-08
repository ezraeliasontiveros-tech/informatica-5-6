def main():
    welcome()
    choice = int(input("Select your order:"))
    get_item(choice)

def welcome():
    print("Welcome to El pato!")
    print("Here's the menu:")
    menu = ["cheeseburger","fries","soda","ice cream","cookie"]
    for food in range(len(menu)):#range hace una lista
        print(f"{food+1}. {menu[food]}")

def get_item(order):
    if order == 1:
        print("🍔")
    elif order == 2:
        print("🍟")
    elif order == 3:
        print("🥤")
    elif order == 4:
        print("🍦")
    elif order == 5:
        print("🍪")
    else:
        print("Not in our menu.")






if __name__=="__main__":
    main()
