def main():
    print("Binary to Decimal Converter")
    print("The porpuse of this program is to be able to read binary numbers and interpret them into a decimal number")
    print()

    binary = int(input("Enter a bynary number:"))
    binary_to_decimal(binary)


def binary_to_decimal(binary):
    binary = [1,2,4,8,16,32,64]
    for num in range(len(binary)):
        print(f"Decimal number:{num*2} + {binary[num]}")



if __name__=="__main__":
    main()
