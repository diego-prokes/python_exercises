if __name__ == '__main__':

    invalid = True
    while invalid:
        f = float(input("\nIngrese la temperatura en grados Fahrenheit: "))
        if (f >= -459.67):
            break
        else:
            print("\n\tLa temperatura ingresada no es físicamente posible.")
    print("\nProcesando\n...\n...\n...\n")
    c = ((5*f)-32)/9
    print("La temperatura en grados Celsius es: ", round(c,2))

