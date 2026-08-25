def main():
    print("EOT PIZZA")
    rating = float(input("rate the restaurant:"))

    if rating >= 4.5:
        print("Pefection")
    elif rating >= 4:
        print("Exellent")
    elif rating >= 3:
        print("good")
    elif rating >= 2:
        print("fair")
    else:
        print("ASQUEROSO")






if __name__=="__main__":
    main()
