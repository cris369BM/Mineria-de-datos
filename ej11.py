import csv
alumnos = []
suma_promedios = 0.0
with open("calificaciones.csv", "r", encoding="utf-8") as archivo:
    
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        Nombre = fila['Nombre']
        Carrera = fila['Carrera']
        
        Parcial1 = float(fila['Parcial1'])
        Parcial2 = float(fila['Parcial2'])
        Parcial3 = float(fila['Parcial3'])
        
        
        promedio = (Parcial1 + Parcial2 + Parcial3) / 3
        
        alumnos.append({
            'Nombre': Nombre,
            'Carrera': Carrera,
            'promedio': promedio
        })
        
        suma_promedios += promedio

cantidad_alumnos = len(alumnos)

if cantidad_alumnos > 0:
    
    promedio_general = suma_promedios / cantidad_alumnos

    alumnos_ordenados = sorted(alumnos, key=lambda x: x['promedio'], reverse=True)
    
    mejor_alumno = alumnos_ordenados[0]
    peor_alumno = alumnos_ordenados[-1]
    
    aprobados = 0
    reprobados = 0
    
    for alumno in alumnos:
        if alumno['promedio'] >= 60.0:  
            aprobados += 1
        else:
            reprobados += 1

    # --- IMPRESIÓN DE RESULTADOS ---
    print(f"--- PROMEDIO GENERAL ---")
    print(f"El promedio general del grupo es: {promedio_general:.2f}")

    print("\n--- MEJOR Y PEOR ALUMNO ---")
    print(f"Mejor: {mejor_alumno['Nombre']} ({mejor_alumno['Carrera']}) con {mejor_alumno['promedio']:.2f}")
    print(f"Peor: {peor_alumno['Nombre']} ({peor_alumno['Carrera']}) con {peor_alumno['promedio']:.2f}")

    print("\n--- APROBADOS Y REPROBADOS ---")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")

    print("\n--- RANKING DE ALUMNOS ---")
    for posicion, alumno in enumerate(alumnos_ordenados, start=1):
        print(f"{posicion}. {alumno['Nombre']} - Carrera: {alumno['Carrera']} - Promedio: {alumno['promedio']:.2f}")

else:
    print("El archivo está vacío o no se encontraron alumnos.")