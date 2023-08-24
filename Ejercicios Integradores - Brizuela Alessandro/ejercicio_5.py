def get_int_iterativo():
    while True:
        try:
            valor = int(input("Ingrese un numero entero (iterativo): "))
            return valor
        except ValueError:
            print("El numero que ingresaste no es valido. Ingrese de nuevo")

def get_int_recursivo():
    try:
        valor = int(input("Ingrese un numero entero (recursivo): "))
        return valor
    except ValueError:
        print("El numero que ingresaste no es valido. Ingrese de nuevo")
        return get_int_recursivo()

int1 = get_int_iterativo()
int2 = get_int_recursivo()
print(f"El numero iterativo que ingresaste fue: {int1}")
print(f"El numero recursivo que ingresaste fue: {int2}")