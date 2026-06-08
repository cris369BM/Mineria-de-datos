import funciones

def main():
    print("--- Prueba Ejercicio 1 ---")
    funciones.saludar_amigo()

    print("\n--- Prueba Ejercicio 2 ---")
    funciones.saludar_nombre("Carlos")

    print("\n--- Prueba Ejercicio 3 ---")
    numero = 5
    resultado_factorial = funciones.calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado_factorial}")

    print("\n--- Prueba Ejercicio 4 ---")
    monto = 1000
    
    print(f"Total factura sin indicar IVA (aplica 21%): ${funciones.calcular_factura(monto)}")
    
    print(f"Total factura indicando 16% de IVA: ${funciones.calcular_factura(monto, 16)}")

    print("\n--- Prueba Ejercicio 5 ---")
    radio = 3
    altura = 10
    print(f"El área del círculo con radio {radio} es: {funciones.area_circulo(radio):.2f}")
    print(f"El volumen del cilindro es: {funciones.volumen_cilindro(radio, altura):.2f}")

if __name__ == "__main__":
    main()