
numero = int(input("Ingresa un número para saber si es primo: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:

    for i in range(2, numero):

        if numero % i == 0:
            es_primo = False  
            break           
        
if es_primo:
    print(f"El número {numero} SÍ es primo.")
else:
    print(f"El número {numero} NO es primo.")
