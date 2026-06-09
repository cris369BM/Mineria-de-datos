tipoPizza = input("Escoge el tipo de pizza: Vegetariana (1) o No vegetariana (2): ")

if tipoPizza == "1":
    ingrediente = input("Escoge un ingrediente: a) Pimiento  b) Tofu: ")

    if ingrediente == "a":
        print("Pizza elegida: Vegetariana")
        print("Ingredientes: Mozzarella, tomate y pimiento")
    elif ingrediente == "b":
        print("Pizza elegida: Vegetariana")
        print("Ingredientes: Mozzarella, tomate y tofu")
    else:
        print("Ingrediente no válido")

elif tipoPizza == "2":
    ingrediente = input("Escoge un ingrediente: a) Peperoni  b) Jamón  c) Salmón: ")

    if ingrediente == "a":
        print("Pizza elegida: No vegetariana")
        print("Ingredientes: Mozzarella, tomate y peperoni")
    elif ingrediente == "b":
        print("Pizza elegida: No vegetariana")
        print("Ingredientes: Mozzarella, tomate y jamón")
    elif ingrediente == "c":
        print("Pizza elegida: No vegetariana")
        print("Ingredientes: Mozzarella, tomate y salmón")
    else:
        print("Ingrediente no válido")

else:
    print("Tipo de pizza no válido")