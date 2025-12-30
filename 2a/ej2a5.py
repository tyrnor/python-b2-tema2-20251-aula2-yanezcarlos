"""
Enunciado:
Explora el análisis de datos mediante la realización de una regresión lineal y la interpolación de un conjunto de datos.
Este ejercicio se centra en el uso de scipy.optimize para llevar a cabo una regresión lineal y en la aplicación de
scipy.interpolate para la interpolación de datos.

Implementa la función linear_regression_and_interpolation(data_x, data_y) que realice lo siguiente:
    - Regresión Lineal: Ajustar una regresión lineal a los datos proporcionados.
    - Interpolación: Crear una interpolación lineal de los mismos datos.

Adicionalmente, implementa la función plot_results(data_x, data_y, results) para graficar los datos originales,
la regresión lineal y la interpolación.

Parámetros:
    - data_x (List[float]): Lista de valores en el eje x.
    - data_y (List[float]): Lista de valores en el eje y correspondientes a data_x.
    - results (Dict): Resultados de la regresión lineal e interpolación.

Ejemplo:
    - Entrada:
        data_x = np.linspace(0, 10, 100)
        data_y = 3 - data_x + 2 + np.random.normal(0, 0.5, 100) # Datos con tendencia lineal y algo de ruido
    - Ejecución:
        results = linear_regression_and_interpolation(data_x, data_y)
        plot_results(data_x, data_y, results)
    - Salida:
        Un gráfico mostrando los datos originales, la regresión lineal y la interpolación.
"""

from scipy import interpolate, optimize
import numpy as np
import matplotlib.pyplot as plt
import typing as t


def linear_regression_and_interpolation(
    data_x: t.List[float], data_y: t.List[float]
) -> t.Dict[str, t.Any]:
    # Write here your code
    
    x = np.array(data_x)
    y = np.array(data_y)

    # ----- Linear regression -----
    def linear_model(x, a, b):
        return a * x + b

    params, _ = optimize.curve_fit(linear_model, x, y)
    slope, intercept = params

    y_regression = linear_model(x, slope, intercept)

    # ----- Interpolation -----
    interp_func = interpolate.interp1d(x, y, kind="linear")
    interpolated_data = interp_func(x)

    return {
        "linear_regression": {
            "slope": slope,
            "intercept": intercept,
            "y_values": y_regression,
        },
        "interpolated_data": interpolated_data,
    }


def plot_results(data_x: t.List[float], data_y: t.List[float], results: t.Dict):
    # Write here your code
    
    x = np.array(data_x)
    y = np.array(data_y)

    plt.figure(figsize=(10, 6))

    # Original data
    plt.scatter(x, y, label="Original Data", alpha=0.6)

    # Linear regression
    plt.plot(
        x,
        results["linear_regression"]["y_values"],
        linestyle="--",
        label="Linear Regression",
    )

    # Interpolation
    plt.plot(
        x,
        results["interpolated_data"],
        label="Linear Interpolation",
        linewidth=2,
    )

    plt.title("Linear Regression and Interpolation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# data_x = np.linspace(0, 10, 100)
# data_y = 3 * data_x + 2 + np.random.normal(0, 2, 100)
# results = linear_regression_and_interpolation(data_x, data_y)
# plot_results(data_x, data_y, results)
