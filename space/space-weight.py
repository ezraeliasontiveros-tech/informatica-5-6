def main():
    weight = float(input("what is the weight in the earth?:"))
    planet = int(input("give me a planet number:"))

    mercury = 1
    venus = 2
    mars = 3
    jupiter = 4
    saturn = 5
    uranus = 6
    neptune = 7

    if weight == mercury:
        weight * 0.38
    elif weight == venus:
        weight * 0.91
    elif weight == mars:
        weight * 0.38
    elif weight == jupiter:
        weight * 2.58
    elif weight == saturn:
        weight * 1.07
    elif weight == uranus:
        weight * 0.89
    elif weight == neptune:
        weight * 1.14
    elif planet > 7:
        print("invalid option")





if __name__=="__main__":
    main()
