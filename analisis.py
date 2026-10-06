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

# 3. Temperatura máxima (si hay empates, se muestran todos)
temp_max = df["temperatura_c"].max()
filas_max = df[df["temperatura_c"] == temp_max]
print(f"\nTemperatura máxima: {temp_max} °C")
print(filas_max[["id_sensor", "fecha_hora", "temperatura_c"]].to_string(index=False))

# 4. Lecturas con alerta (> 85 °C)
alertas = df[df["temperatura_c"] > UMBRAL_C]
print(f"\nLecturas con alerta (> {UMBRAL_C} °C): {len(alertas)}")

# 5. Planta(s) con más alertas (si hay empates, se muestran todas)
conteo = alertas["planta"].value_counts()
if conteo.empty:
    print("No hay alertas.")
else:
    maximo = conteo.max()
    print("Planta(s) con más alertas:")
    print(conteo[conteo == maximo].to_string())