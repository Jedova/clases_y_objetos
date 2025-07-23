class Te:

    ##Atributo de clase##
    duracion = 365  #total de días de 1 años

    @staticmethod
    def obtener_preparacion_y_recomendacion(sabor: int): ## recomendaciones de consumo en horarios##
        if sabor == 1:
            return 3, "Se recomienda consumir al desayuno"
        elif sabor == 2:
            return 5, "Se recomienda consumir al medio día"
        elif sabor == 3:
            return 6, "Se recomienda consumir al atardecer"
        else:
            return None, "Sabor no válido"

    @staticmethod
    def obtener_precio(formato: int): ##precios asociados##
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return None  # Formato no válido
