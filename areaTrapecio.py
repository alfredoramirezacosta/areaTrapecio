def area_trapecio(base_mayor, base_menor, altura):
    return (base_mayor + base_menor) * altura / 2

if __name__ == "__main__":
    b_mayor = float(input("Introduce la medida de la Base Mayor: "))
    b_menor = float(input("Introduce la madida de la Base Menor: "))
    h = float(input("introduce la medida de la Altura: "))
    resultado = area_trapecio(b_mayor, b_menor, h)
    print(f"El area del Trapecio es: {resultado}")