# Función para calcular la liquidación de un empleado
def calcular_liquidacion(nombre, dias, salario):
    # Se realiza el calculo
    prima = (salario * dias) / 360
    cesantias = (salario * dias) / 360
    intereses_cesantias = (cesantias * 0.12) * (dias / 360)
    vacaciones = (salario * dias) / 720

    # Liquidacion
    liquidacion = prima + cesantias + intereses_cesantias + vacaciones

    # Resultado
    return {
        "nombre": nombre,
        "dias": dias,
        "salario": salario,
        "prima": prima,
        "cesantias": cesantias,
        "intereses_cesantias": intereses_cesantias,
        "vacaciones": vacaciones,
        "liquidacion": liquidacion
    }

#  Ingresar datos desde teclado
nombre = input("Nombre : ")
dias = int(input("Días: "))
salario = float(input("Salario: "))

# Se calcula la liquidación
resultados = calcular_liquidacion(nombre, dias, salario)

# se muetran los resultados
print(f"Señor {resultados['nombre']} para los {resultados['dias']} "
      f"días laborados y salario ${resultados['salario']:.2f}, su liquidación se compone así:")
print(f"Prima: ${resultados['prima']:.2f}")
print(f"Cesantía: ${resultados['cesantias']:.2f}")
print(f"Intereses cesantías: ${resultados['intereses_cesantias']:.2f}")
print(f"Vacaciones: ${resultados['vacaciones']:.2f}")
print(f"Liquidación: ${resultados['liquidacion']:.2f}")
