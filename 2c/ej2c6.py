"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de componentes principales (PCA) utilizando
`sklearn.decomposition.PCA` en el conjunto de datos de viviendas. Este conjunto de datos contiene varias características
de viviendas en áreas suburbanas de Boston, y el objetivo es reducir la dimensionalidad de los datos para identificar
las principales componentes que explican la mayor parte de la varianza en el conjunto de datos.

Las funciones a desarrollar son:
1. Preparar los datos: `prepare_data_for_pca(file_path: str)` que lee el archivo CSV y prepara los datos eliminando
cualquier característica no numérica. Se debe saltar las primeras 14 filas del archivo CSV, que contienen información
adicional sobre el conjunto de datos.
2. Realizar PCA: `perform_pca(data, n_components: int)` que realiza PCA en los datos preparados, reduciendo a
`n_components` número de dimensiones, en este caso a 4 dimensiones.
3. Visualizar los resultados: `plot_pca_results(pca)` que visualiza los resultados de PCA, incluyendo la varianza
explicada por cada componente principal.

Parámetros:
    file_path (str): Ruta al archivo CSV que contiene los datos del dataset de viviendas.
    n_components (int): Número de componentes principales a retener en el análisis PCA.

Ejemplo de uso:
    pca = perform_pca(data, 4)
    plot_pca_results(pca)

Salida esperada:
    Una visualización de la varianza explicada por los componentes principales y, opcionalmente, una transformación de
    los datos originales proyectada en las principales componentes.
"""

from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def prepare_data_for_pca(file_path: str) -> pd.DataFrame:
    # Write here your code
    df = pd.read_csv(file_path, skiprows=14)
    numeric_df = df.select_dtypes(include=["number"])
    if "MEDV" in numeric_df.columns:
        numeric_df = numeric_df.drop(columns=["MEDV"])
    return numeric_df


def perform_pca(data: pd.DataFrame, n_components: int) -> PCA:
    # Write here your code
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    pca = PCA(n_components=n_components)
    pca.fit(scaled_data)
    return pca


def plot_pca_results(pca: PCA) -> tuple:
    explained_variance = pca.explained_variance_ratio_

    fig, ax = plt.subplots()
    ax.bar(
        range(1, len(explained_variance) + 1),
        explained_variance
    )

    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    ax.set_title("PCA Explained Variance")

    plt.tight_layout()

    return fig, ax


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     FILE_PATH = current_dir / "data/housing.csv"
#     dataset = prepare_data_for_pca(FILE_PATH)
#     pca = perform_pca(dataset, 4)
#     _, _ = plot_pca_results(pca)
