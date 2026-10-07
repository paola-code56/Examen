# Informe — Manejo Masivo de Datos

## 5. Las 5 V aplicadas al proyecto

| V | Relación con el sistema de sensores | Ejemplo concreto | ¿CSV actual o ampliación? |
| --- | --- | --- | --- |
| Volumen | Cantidad de mediciones acumuladas | 100,000 filas hoy; miles de sensores después | Ambos (100,000 en el CSV; miles de sensores es ampliación) |
| Velocidad | Ritmo al que llegan los datos | 1 lectura/minuto por sensor hoy; 1/segundo después | CSV: 1 por minuto; 1 por segundo es ampliación |
| Variedad | Distintos formatos de datos | Tabla CSV hoy; JSON, fotos y reportes de mantenimiento después | CSV: solo tabular; el resto es ampliación |
| Veracidad | Calidad y confiabilidad de las lecturas | Valores nulos, duplicados o fuera de rango por fallas del sensor | [Revisa si tu CSV tiene nulos/duplicados y dilo aquí] |
| Valor | Utilidad de los datos para decidir | Detectar temperaturas > 85 °C para actuar antes de una falla | CSV: alertas calculadas; predicción es ampliación |

## 6. Tipos de datos y procesamiento tradicional

- CSV de sensores: **estructurado** (filas y columnas fijas).
- Mensaje JSON de un sensor: **semiestructurado** (etiquetas y campos, esquema flexible).
- Fotografía de una máquina: **no estructurado**.
- Texto libre de un reporte de mantenimiento: **no estructurado**.

**100,000 registros no son automáticamente Big Data:** caben en la memoria de una computadora normal y Python/pandas los procesa en segundos. Big Data depende de volumen, velocidad y variedad juntos y de que las herramientas tradicionales ya no alcancen.

**Limitaciones al escalar:** el archivo ya no cabría en memoria, el procesamiento en una sola máquina sería lento, no se puede reaccionar en segundos leyendo un archivo, y el CSV no maneja fotos ni texto libre.

## 7. Batch y Streaming

- Lo que hice es **procesamiento por lotes (batch)**: el archivo ya estaba completo y lo analicé de una vez.
- Alerta a los pocos segundos de una lectura > 85 °C: **streaming**, porque el resultado se necesita casi en el momento en que llega el dato.
- Resumen al terminar el día: **batch**, porque se puede esperar a tener todos los datos del día y no requiere inmediatez.

## 8. Lambda y Kappa

**Escenario A → Lambda** (ruta batch para recalcular el historial + ruta rápida para lo reciente).

```
Sensores -> Ingesta -> Capa batch (historial) -----> Vista batch --\
                   \                                                 -> Consulta
                    -> Capa rápida (recientes) ----> Vista tiempo real -/
```

**Escenario B → Kappa** (una sola lógica de streaming y el registro de eventos permite reprocesar).

```
Sensores -> Registro de eventos (log conservado) -> Procesamiento de streaming -> Resultados
                          ^                                  |
                          \---- reprocesar desde el log -----/
```

Justificación: [explica en 2-3 líneas: Lambda por dos rutas separadas; Kappa por una sola lógica y reprocesamiento desde el log].

## 9. Analítica

- **Descriptiva (usa tus resultados reales):**
  1. [Ej.: La planta X tiene la temperatura promedio más alta: __ °C]
  2. [Ej.: Hay __ lecturas > 85 °C y la planta Y concentra más alertas con __]
- **Predictiva:** ¿Qué máquinas podrían fallar en los próximos días? Datos adicionales: historial de fallas, mantenimientos, edad de la máquina, carga de trabajo, temperatura ambiente.
- **Prescriptiva:** Si se prevé riesgo en una máquina, adelantar su inspección de mantenimiento. Antes de decidir revisaría: historial de fallas y mantenimientos, si las alertas son persistentes o puntuales, el estado del sensor y el costo de detener la máquina.

Nota: una lectura > 85 °C es una alerta del ejercicio; por sí sola no demuestra que una máquina vaya a fallar.
