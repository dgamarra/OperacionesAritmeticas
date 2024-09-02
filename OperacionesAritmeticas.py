class OperacionesAritmeticas():
    def ingresoNumeros(self):
        numero1 = float(input("Ingrese sumando uno: "))
        numero2 = float(input("Ingrese sumando dos: "))
        return numero1, numero2


    def suma(self, numero1, numero2):
        return numero1 + numero2
