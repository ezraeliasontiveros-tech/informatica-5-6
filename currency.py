def main():
    pesos = float(input("What do you have left in pesos?:"))
    soles = float(input("What do you have left in soles?:"))
    reais = float(input("What do you have left in reais?:"))


    cu = (0.19*reais)
    su = (0.30*soles)
    ru = (0.00032*pesos)

    eu = (cu + su + ru)
    round(eu,2)
    print("USD:",eu)


    cm = (0.0054*pesos)
    sm = (5.07*soles)
    rm = (3.27*reais)

    mx = (cm + sm + rm)
    round(mx,2)
    print("MXN:",mx)




if __name__=="__main__":
    main()
