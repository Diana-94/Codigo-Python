def ingresar_datos():
    # Ingresar datos
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    # Ingresar números enteros en un arreglo
    num_elementos = int(input("Ingrese la cantidad de números enteros para el arreglo: "))
    arreglo_enteros = []
    for i in range(num_elementos):
        entero = int(input(f"Ingrese el número entero {i + 1}: "))
        arreglo_enteros.append(entero)

    datos = {"nombre": nombre, "edad": edad, "arreglo_enteros": arreglo_enteros}

    return datos

def imprimir_datos(datos):
    print("\nDatos ingresados:")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print("Arreglo de enteros:", datos['arreglo_enteros'])

def ordenar_por_seleccion(arreglo):
    n = len(arreglo)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j

        # Intercambio
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]

if __name__ == "__main__":
    datos_ingresados = ingresar_datos()

    print("\nDatos ingresados:")
    imprimir_datos(datos_ingresados)

    # Ordenar el arreglo de enteros por selección
    arreglo_enteros = datos_ingresados['arreglo_enteros']
    ordenar_por_seleccion(arreglo_enteros)

    print("\nArreglo de enteros después de ordenar por selección:")
    print(arreglo_enteros)
