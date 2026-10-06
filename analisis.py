from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent
RUTA_CSV = BASE / "data" / "sensores_industriales.csv"
UMBRAL_C = 85

df = pd.read_csv(RUTA_CSV)

# 1. Registros y sensores distintos
print("Registros:", len(df))
print("Sensores distintos:", df["id_sensor"].nunique())

# 2. Temperatura promedio por planta
promedios = df.groupby("planta")["temperatura_c"].mean().round(2)
print("\nTemperatura promedio por planta:")
print(promedios.to_string())