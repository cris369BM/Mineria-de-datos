import math

def saludar_amigo():
    print("¡Hola amigo!")

def saludar_nombre(nombre):
    print(f"¡hola {nombre}!")

def calcular_factorial(n):
    if n < 0:
        return "El número debe ser positivo."
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def calcular_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva + (cantidad_sin_iva * (porcentaje_iva / 100))
    return total

def area_circulo(radio):
    return math.pi * (radio ** 2)

def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)
    return area_base * altura