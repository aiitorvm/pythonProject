# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def main ():
    num = int(input("Introdueix el numero del mes "))
    while num < 1 or num > 12:
        num = int(input("Introdueix el numero del mes "))

    match num:
        case 1:
            print ("Gener te 31 dies")
        case 2:
            print("Febrer te 28 dies")
        case 3:
            print("Març te 31 dies")
        case 4:
            print("Abril te 30 dies")
        case 5:
            print("Maig te 31 dies")
        case 6:
            print("Juny te 30 dies")
        case 7:
            print("Juliol te 31 dies")
        case 8:
            print("Agost te 31 dies")
        case 9:
            print("Septembre te 30 dies")
        case 10:
            print("Octubre te 31 dies")
        case 11:
            print("Novembre te 30 dies")
        case 12:
            print("Decembre te 31 dies")
"""
"""
def main ():
    num1 = int(input("Introdueix el numero1: "))
    num2 = int(input("Introdueix el numero2: "))
    aux = num1
    num1 = num2
    num2 = aux
    print("Estos son los numeros intercambiados:", num1, num2)
"""


# Press the green button in the gutter to run the script.
"""
def main ():
    num = int(input("Introduce un número: "))
    resultado, suma = 0, 0
    while num < 0:
        num = int(input("Introduce un número: "))
    while num >= resultado + suma:
        resultado = suma + resultado
        print(suma, "->", resultado)
        suma += 1
"""
"""
def main():
    print(input("Pon una frase:")[:: - 1])
"""
def main():
    llista = list ()
    llista.append(input("Pon que quieres añadir: "))
    print(llista)




















if __name__ == '__main__':
    main()

