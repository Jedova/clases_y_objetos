from te import Te

##Las opciones del usuario son ##
sabor = int(input("Seleccione el sabor de té considerando: 1: Té negro; 2: Té verde; 3: Agua de hierbas." \
" Ingrese el número del sabor deseado: "))

formato = int(input("Ingrese el formato (300 o 500 gramos): "))

# Obtener valores desde métodos estáticos
tiempo, recomendacion = Te.obtener_preparacion_y_recomendacion(sabor)
precio = Te.obtener_precio(formato)

# Obtener nombre del sabor
sabores = {1: "Té negro", 2: "Té verde", 3: "Agua de hierbas"}
nombre_sabor = sabores.get(sabor, "Sabor no válido")

# Mostrar resumen del pedido
print("\n--- Detalle del pedido ---")
print(f"Sabor: {nombre_sabor}")
print(f"Formato: {formato} gr")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")
