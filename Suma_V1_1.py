def ingresoNumeros():
    numero1 = float(input("Ingrese sumando uno: "))
    numero2 = float(input("Ingrese sumando dos: "))
    return numero1, numero2


def suma(numero1, numero2):
    return numero1 + numero2

if __name__ == '__main__':
    num1, num2 = ingresoNumeros()
    print(f"{num1} + {num2} = {suma(num1, num2)}")
