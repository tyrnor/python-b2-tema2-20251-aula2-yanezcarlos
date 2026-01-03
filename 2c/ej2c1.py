"""
Enunciado:
Desarrolla un conjunto de funciones para la manipulación de datos utilizando Pandas. El objetivo es 
trabajar con un DataFrame de un archivo CSV que contiene información sobre calificaciones y realizar la selección 
de columnas por nombre e índice y filas que cumplan múltiples condiciones.

Las funciones y escenarios a desarrollar son:

1. Seleccionar columnas por nombre o índice y opcionalmente filas por rango:
    - `select_rows_and_columns(df: pd.DataFrame, columns: Union[List[str], List[int]], rows: Optional[slice] = None) -> pd.DataFrame`
      Esta función permite seleccionar columnas específicas por nombre o índice y opcionalmente filas por un rango especificado.
      Si no se especifica un rango de filas, se seleccionarán todas las filas por defecto.

2. Seleccionar filas que cumplan con una o múltiples condiciones:
    - `select_rows_with_conditions(df: pd.DataFrame, conditions: Union[str, List[str]]) -> pd.DataFrame`
      Permite seleccionar filas que cumplan con una o múltiples condiciones dadas en formato de cadena.

Parámetros:
    - df (pd.DataFrame): DataFrame original.
    - columns (Union[List[str], List[int]]): Nombres o índices de las columnas a seleccionar.
    - rows (Optional[slice]): Rango de filas a seleccionar, especificado como un objeto slice. Por defecto, selecciona todas las filas.
    - conditions (Union[str, List[str]]): Una o múltiples condiciones en formato de cadena.

Ejemplo:
    selected_columns_and_rows = select_rows_and_columns(df_grades, ['Name', 'Maths', 'History'], rows=slice(5, 10))
    selected_rows = select_rows_with_conditions(df_grades, ['English > 50', 'Maths >= 60', 'Geography > 55'])

Salida Esperada:
- DataFrame resultante después de seleccionar las columnas específicas por nombre e índice y opcionalmente filas por rango.
- DataFrame resultante después de seleccionar las filas que cumplen con las condiciones.
"""

from pathlib import Path
from typing import List, Union, Optional
import pandas as pd


def select_rows_and_columns(
    df: pd.DataFrame, columns: Union[List[str], List[int]], rows: Optional[slice] = None
) -> pd.DataFrame:
    # Write here your code
    if all(isinstance(col, int) for col in columns):
        selected_df = df.iloc[:, columns]   
    else:
        selected_df = df[columns]

    if rows is not None:
        selected_df = selected_df.iloc[rows]

    return selected_df


def select_rows_with_conditions(
    df: pd.DataFrame, conditions: Union[str, List[str]]
) -> pd.DataFrame:
    # Write here your code
    if isinstance(conditions, str):
        conditions = [conditions]   
    
    query_str = " & ".join(f"({cond})" for cond in conditions)
    filtered_df = df.query(query_str)
    return filtered_df


# Para probar el código, descomenta las siguientes líneas y asegúrate de tener un archivo CSV 'data/grades.csv'
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     FILE_PATH = current_dir / "data/grades.csv"
#     df_grades = pd.read_csv(FILE_PATH)
#     selected_columns_and_rows = select_rows_and_columns(
#         df_grades, ["Name", "Maths", "History"], rows=slice(5, 10)
#     )
#     selected_rows = select_rows_with_conditions(
#         df_grades, ["English > 50", "Maths >= 60", "Geography > 55"]
#     )
#     print("DataFrame Original:\n", df_grades.head())
#     print(
#         "DataFrame with Selected Columns and Rows:\n", selected_columns_and_rows.head()
#     )
#     print("DataFrame with Rows that Meet Conditions:\n", selected_rows.head())
