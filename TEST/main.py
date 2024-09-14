#import everything from file.py
from operesta import resta
from opersuma import suma
def main():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")

    opcion = input("Elige una opción (1/2): ")

    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = suma(a, b)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = resta(a, b)
        print(f"El resultado de la resta es: {resultado}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
