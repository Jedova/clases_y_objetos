from te import Te

# Crear dos instancias de la clase Te
te1 = Te()
te2 = Te()

# Obtener y almacenar el tipo
tipo1 = type(te1)
tipo2 = type(te2)

# Mostrar tipos
print(f"El tipo de te1: {tipo1}")
print(f"El tipo de te2: {tipo2}")

# Comparar tipos
if tipo1 == tipo2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
