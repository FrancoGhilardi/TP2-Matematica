import datetime
from itertools import product
from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

# Función para verificar si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# A. OPERACIONES CON DNIs
def operaciones_con_dnis():
    cantidad = 2
    print(Fore.YELLOW + f"Se solicitarán {cantidad} DNIs.")
    dnis = []
    conjuntos_digitos = []

    for i in range(cantidad):
        dni = input(Fore.YELLOW + f"Ingrese el DNI #{i+1} (sin puntos ni guiones): ")
        dnis.append(dni)
        conjuntos_digitos.append(set(dni))

    print(Fore.CYAN + "\n--- Operaciones con conjuntos ---")
    union = set.union(*conjuntos_digitos)
    interseccion = set.intersection(*conjuntos_digitos)
    diferencia = conjuntos_digitos[0].difference(*conjuntos_digitos[1:])
    diferencia_simetrica = set.symmetric_difference(*conjuntos_digitos)

    print(Fore.GREEN + "Unión de dígitos:", union)

    if interseccion:
        print(Fore.GREEN + "Intersección de dígitos:", interseccion)
    else:
        print(Fore.RED + "Intersección de dígitos: No hay dígitos en común.")

    if diferencia:
        print(Fore.GREEN + "Diferencia (primer DNI - resto):", diferencia)
    else:
        print(Fore.RED + "Diferencia (primer DNI - resto): No hay diferencias.")

    if diferencia_simetrica:
        print(Fore.GREEN + "Diferencia simétrica:", diferencia_simetrica)
    else:
        print(Fore.RED + "Diferencia simétrica: Los DNIs tienen exactamente los mismos dígitos.")

    print(Fore.CYAN + "\n--- Frecuencia de dígitos y suma total ---")
    for dni in dnis:
        print(Fore.YELLOW + f"\nDNI: {dni}")
        frecuencia = {str(d): 0 for d in range(10)}
        suma = 0
        for digito in dni:
            frecuencia[digito] += 1
            suma += int(digito)
        print(Fore.GREEN + "Frecuencia de dígitos:", frecuencia)
        print(Fore.GREEN + "Suma total de dígitos:", suma)

    print(Fore.CYAN + "\n--- Evaluaciones lógicas ---")
    if interseccion:
        print(Fore.MAGENTA + f"Dígito(s) compartido(s): {' '.join(interseccion)}")

    for i, conjunto in enumerate(conjuntos_digitos):
        if len(conjunto) > 6:
            print(Fore.MAGENTA + f"Diversidad numérica alta en el DNI #{i+1}: {dnis[i]}")

# B. OPERACIONES CON AÑOS DE NACIMIENTO
def operaciones_con_anios():
    print(Fore.CYAN + "\n=== Operaciones con Años de Nacimiento ===")
    while True:
        try:
            cantidad = int(input(Fore.YELLOW + "¿Cuántos años de nacimiento desea ingresar? "))
            if cantidad >= 1:
                break
            else:
                print(Fore.RED + "Por favor, ingrese un número mayor o igual a 1.")
        except ValueError:
            print(Fore.RED + "Entrada inválida. Ingrese un número entero.")
    anios = []

    for i in range(cantidad):
        anio = int(input(Fore.YELLOW + f"Ingrese el año de nacimiento #{i+1}: "))
        anios.append(anio)

    pares = sum(1 for a in anios if a % 2 == 0)
    impares = len(anios) - pares
    print(Fore.GREEN + f"\nCantidad de años pares: {pares}")
    print(Fore.GREEN + f"Cantidad de años impares: {impares}")

    if all(a > 2000 for a in anios):
        print(Fore.MAGENTA + "Grupo Z")

    if any(es_bisiesto(a) for a in anios):
        print(Fore.MAGENTA + "Tenemos un año especial")

    print(Fore.CYAN + "\n--- Producto cartesiano con edades actuales ---")
    anio_actual = datetime.datetime.now().year
    edades = [anio_actual - a for a in anios]
    producto = list(product(anios, edades))
    for par in producto:
        print(Fore.GREEN + str(par))

# MENÚ PRINCIPAL
def mostrar_menu():
    print(Fore.CYAN + "\n=== Menú de opciones ===")
    print("1. Operaciones con DNIs")
    print("2. Operaciones con años de nacimiento")
    print("3. Salir")

def main():
    print(Fore.CYAN + "=== Programa de Operaciones ===")
    while True:
        mostrar_menu()
        opcion = input(Fore.YELLOW + "Seleccione una opción (1-3): ").strip()

        if opcion == '1':
            operaciones_con_dnis()
        elif opcion == '2':
            operaciones_con_anios()
        elif opcion == '3':
            print(Fore.CYAN + "¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción inválida. Intente nuevamente.")


main()
