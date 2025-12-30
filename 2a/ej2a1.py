"""
Enunciado:
Simula el lanzamiento de un dado un número determinado de veces y calcula la probabilidad 
de cada resultado. Implementa la función 'simulate_dice_rolls(n)' que simule el lanzamiento 
de un dado 'n' veces y retorne un diccionario con las probabilidades de cada resultado (del 1 al 6).

La función debe usar la generación de números aleatorios para simular cada lanzamiento y 
debe calcular la probabilidad de cada resultado como la frecuencia relativa del mismo.

Parámetros:
    number (int): Número de veces que se lanzará el dado

Ejemplo:
    Entrada:
    num_rolls = 10000
    simulate_dice_rolls(num_rolls)

    Salida:
    Un diccionario donde las llaves son los resultados posibles (1, 2, 3, 4, 5, 6) y los valores 
    son las probabilidades de cada resultado. Por ejemplo: {1: 0.166, 2: 0.167, 3: 0.167, 4: 0.167, 5: 0.166, 6: 0.167}
"""

import numpy as np


def simulate_dice_rolls(number: int) -> dict:
    # Write here your code
    if number <= 0:
        raise ValueError("El número de lanzamientos debe ser un entero positivo.")
    
    rolls = np.random.randint(1, 7, size=number)

    counts = np.bincount(rolls, minlength=7)[1:]

    probabilities = {i + 1: counts[i] / number for i in range(6)}

    return probabilities

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# num_rolls = 10000
# print(simulate_dice_rolls(num_rolls))
