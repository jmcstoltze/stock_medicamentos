
from medicamento import Medicamento

opcion_ingreso = int(input("¿Desea agregar un medicamento?"
"\n1. Sí\n2. No\n"))

# Lista que almacena los objetos medicamento
ingresados = []

# Ciclo del cual solo se pueda salir cuando la opción sea diferente de 1
while opcion_ingreso == 1:
    nombre = input("\nIngrese nombre del medicamento:\n")
    stock = int(input("\nIngrese stock del medicamento:\n"))
    m = Medicamento(nombre, stock)

    # Si medicamento existe en la lista 
    if m in ingresados:

        # Sumar el stock al medicamento existente
        indice = ingresados.index(m)
        ingresados[indice] += m

        # Código modificado. Llama a los atributos del objeto ya existente
        nombre = ingresados[indice].nombre
        precio_bruto = ingresados[indice].precio_bruto
        precio_final = ingresados[indice].precio_final
        stock = ingresados[indice].stock

        # Imprime atributos
        print(f"\n***** DATOS MEDICAMENTO {nombre} *****")
        print(f"PRECIO BRUTO: ${precio_bruto}")
        print(f"PRECIO FINAL: ${precio_final}")
        print(f"STOCK: {stock}")
        
    # Si no existe lo agrega a la lista e imprime sus atributos
    else:
        ingresados.append(m)
        precio_bruto = int(input("\nIngrese precio bruto del medicamento:\n"))
        m.precio = precio_bruto

        print(f"\n***** DATOS MEDICAMENTO {m.nombre} *****")
        print(f"PRECIO BRUTO: ${m.precio_bruto}")

        # Si tiene descuento lo imprime
        if m.descuento:
            print(f"DESCUENTO: {m.descuento*100}%")

        print(f"PRECIO FINAL: ${m.precio_final}")
        print(f"STOCK: {m.stock}")
        
    # Imprime el número de medicamentos de la lista
    print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")
    opcion_ingreso = int(input("¿Desea agregar un medicamento?"
                               "\n1. Sí\n2. No\n"))
    
# Imprimir lista de medicamentos (objetos)
    print(ingresados)

# Imprime lista de medicamentos (objetos)
for index, ing in enumerate(ingresados):
    print(ing)

# Imprime atributos de cada objetos
for index, ing in enumerate(ingresados):
    print()
    print(f"Medicamento {index + 1}:")
    print(f"Nombre: {ing.nombre}")
    print(f"Stock: {ing.stock}")
    print(f"Precio bruto: {ing.precio_bruto}")
    print(f"Precio final: {ing.precio_final}")
    print(f"Descuento: {ing.descuento}")
    