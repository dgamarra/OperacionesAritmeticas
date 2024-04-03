def gcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números enteros positivos utilizando el algoritmo de Euclides.

    Args:
    a (int): El primer número entero positivo.
    b (int): El segundo número entero positivo.

    Returns:
    int: El MCD de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a


# Función para validar si el número ingresado es positivo
def validar_numero(num):
    try:
        num = int(num)
        if num <= 0:
            print("Por favor, ingrese un número entero positivo.")
            return False, None
        return True, num
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return False, None


# Solicitar entrada de usuario para el primer número
while True:
    num1 = input("Ingrese el primer número entero positivo: ")
    valido, num1 = validar_numero(num1)
    if valido:
        break

# Solicitar entrada de usuario para el segundo número
while True:
    num2 = input("Ingrese el segundo número entero positivo: ")
    valido, num2 = validar_numero(num2)
    if valido:
        break

# Calcular y mostrar el MCD
print("El Máximo Común Divisor de", num1, "y", num2, "es:", gcd(num1, num2))
