# Análisis de sensores industriales

## Objetivo

Analizar con Python un archivo CSV con mediciones de temperatura y vibración de sensores instalados en cuatro plantas industriales, identificar las lecturas con alerta de temperatura (mayor que 85 °C) y exportarlas a un archivo aparte.

Proyecto del examen práctico de Manejo Masivo de Datos, primer parcial.

## Datos

**Los datos son simulados.** El archivo `data/sensores_industriales.csv` contiene 100,000 mediciones, una por fila, con estas columnas:

| Columna | Significado |
| --- | --- |
| `id_registro` | Identificador de la medición |
| `fecha_hora` | Fecha y hora de la lectura |
| `id_sensor` | Identificador del sensor |
| `planta` | Planta donde está instalado |
| `temperatura_c` | Temperatura en grados Celsius |
| `vibracion_mm_s` | Vibración en milímetros por segundo |

Para este ejercicio, una alerta de temperatura es una lectura mayor que 85 °C. Es una regla didáctica del examen.

## Requisitos

- Python 3.10 o superior
- Git
- Biblioteca `pandas` (versión fijada en `requirements.txt`)

## Instalación

```powershell
git clone [https://github.com/paola-code56/Examen.git]
cd [Examen]
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecución

```powershell
python analisis.py
```

El programa imprime en pantalla:

1. Cantidad de registros y de sensores distintos.
2. Temperatura promedio por planta.
3. Temperatura máxima, con sensor y fecha (todos los empates).
4. Número de lecturas con alerta (> 85 °C).
5. Planta o plantas con más alertas.

Además, genera `resultados/alertas.csv` con todas las lecturas con alerta y las columnas originales.

## Estructura del proyecto

```
├── analisis.py
├── data/sensores_industriales.csv
├── resultados/alertas.csv
├── evidencias/
├── informe.md
├── requirements.txt
└── README.md
```