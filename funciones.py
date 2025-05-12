# ------------------------------------------
# ¿Qué es una función en Python?
# ------------------------------------------
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define con la palabra clave 'def' seguida del nombre de la función y paréntesis.

# ------------------------------------------
# 1. Función básica sin parámetros ni retorno
def saludar():
    print("¡Hola! Esta es una función simple sin parámetros ni retorno.")

saludar()  # Llamada a la función

# ------------------------------------------
# 2. Función con parámetros (entrada de datos)
def saludar_nombre(nombre):
    print(f"¡Hola, {nombre}!")

saludar_nombre("Carlos")

# ------------------------------------------
# 3. Función con valor de retorno (salida de datos)
def sumar(a, b):
    resultado = a + b
    return resultado

suma = sumar(3, 5)
print("Resultado de sumar(3, 5):", suma)

# ------------------------------------------
# 4. Función con valores por defecto
def saludar_con_estilo(nombre="amigo"):
    print(f"¡Hola, {nombre}! ¿Cómo estás?")

saludar_con_estilo()
saludar_con_estilo("Ana")

# ------------------------------------------
# 5. Función con múltiples retornos
def operaciones_basicas(x, y):
    suma = x + y
    resta = x - y
    return suma, resta

suma, resta = operaciones_basicas(10, 4)
print("Suma:", suma)
print("Resta:", resta)

# ------------------------------------------
# 6. Función que llama a otra función
def mostrar_resultados(a, b):
    s, r = operaciones_basicas(a, b)
    print(f"Resultados entre {a} y {b} => Suma: {s}, Resta: {r}")

mostrar_resultados(7, 2)

# ------------------------------------------
# 7. Funciones lambda (funciones anónimas y cortas)
multiplicar = lambda x, y: x * y
print("Multiplicar con lambda:", multiplicar(4, 6))

# ------------------------------------------
# 8. Documentación de funciones con docstrings
def dividir(a, b):
    """
    Esta función divide el número a entre b.
    Parámetros:
        a (float): numerador
        b (float): denominador
    Retorna:
        float: resultado de la división
    """
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

print(dividir(10, 2))
print(dividir.__doc__)  # Muestra la documentación de la función

# ------------------------------------------
# 9. Funciones como argumentos
def aplicar_funcion(funcion, valor):
    return funcion(valor)

doble = lambda x: x * 2
print("Aplicar función doble a 5:", aplicar_funcion(doble, 5))

# ------------------------------------------
# 10. Función dentro de otra función (closures)
def crear_saludo(persona):
    def saludo():
        return f"¡Hola, {persona}!"
    return saludo

mi_saludo = crear_saludo("Lucía")
print(mi_saludo())  # Imprime el saludo generado internamente
