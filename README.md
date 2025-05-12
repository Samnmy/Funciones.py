# Funciones en Python

Este archivo contiene ejemplos de diversas funciones en Python, con explicaciones detalladas de su uso y características. Las funciones son bloques de código reutilizables que realizan tareas específicas. Se definen usando la palabra clave `def`.

## Contenido

1. [Función básica sin parámetros ni retorno](#función-básica-sin-parámetros-ni-retorno)
2. [Función con parámetros](#función-con-parámetros)
3. [Función con valor de retorno](#función-con-valor-de-retorno)
4. [Función con valores por defecto](#función-con-valores-por-defecto)
5. [Función con múltiples retornos](#función-con-múltiples-retornos)
6. [Función que llama a otra función](#función-que-llama-a-otra-función)
7. [Funciones lambda](#funciones-lambda)
8. [Documentación de funciones con docstrings](#documentación-de-funciones-con-docstrings)
9. [Funciones como argumentos](#funciones-como-argumentos)
10. [Función dentro de otra función (closures)](#función-dentro-de-otra-función-closures)

## 1. Función básica sin parámetros ni retorno

Una función simple que no recibe parámetros ni devuelve un valor.

```python
def saludar():
    print("¡Hola! Esta es una función simple sin parámetros ni retorno.")
    
saludar()
