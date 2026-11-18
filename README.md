# Análisis de la cobertura periodística de La República

Proyecto final de **DS3021 Análisis Computacional de Datos** (UTEC, 2026-1) · Grupo 3 · Parte II

Se parte de 1 116 noticias de larepublica.pe recopiladas por scraping en la Parte I. El repositorio contiene el proceso que las limpia, integra y transforma, y el análisis que mide los sesgos de la colección: concentración temporal, confiabilidad de la fecha y la hora, y diferencias de estilo entre áreas editoriales.

**Resultados principales**
- El 43,4 % de las noticias es de agosto y septiembre de 2026; la composición por sección cambia mucho con el año (V de Cramér = 0,61).
- `fecha` nunca es anterior a la fecha de la URL, difiere en el 38,4 % de los casos y llega a 1 632 días: puede ser fecha de actualización.
- El estilo del titular (comillas, cifras, preguntas) y el horario dependen del área editorial.

## Estructura

```
├── data/           CSV original, CSV final y base SQLite
├── notebooks/      01_preprocesamiento.ipynb · 02_analisis_visualizacion.ipynb
├── docs/           Diccionarios de datos (inicial y final)
├── results/        Indicadores, resúmenes y pruebas estadísticas
├── figures/        14 gráficos generados por los notebooks
├── reports/        Informe final (PDF y fuente LaTeX)
├── presentacion/   Presentación (PPTX y PDF) y guion de exposición
├── run_all.py      Ejecuta todo el pipeline
└── requirements.txt
```

## Cómo reproducir

Requiere Python 3.10 o superior y no necesita conexión a internet.

```bash
git clone https://github.com/josueTori-UTEC/ACD-Analisis-Noticias-LaRepublica.git
cd ACD-Analisis-Noticias-LaRepublica
pip install -r requirements.txt
python run_all.py
```

`run_all.py` ejecuta los dos notebooks en orden. También se pueden abrir en Jupyter y correr celda por celda (primero el 01 y luego el 02).

| Paso | Entrada | Salida |
|---|---|---|
| `01_preprocesamiento.ipynb` | `data/noticias_larepublica_original.csv` | `data/noticias_larepublica_final.csv`, `data/noticias_larepublica.db`, `results/indicadores.json`, `results/resumen_*.csv`, `figures/14_pipeline.png` |
| `02_analisis_visualizacion.ipynb` | `data/noticias_larepublica_final.csv` | `figures/01…13_*.png`, `results/pruebas_estadisticas.csv` |

## Datos

- **Original:** 1 116 filas y 7 columnas (`tag`, `titulo`, `longitud_titulo`, `url`, `autor`, `hora`, `fecha`).
- **Final:** 1 116 filas y 31 columnas (24 derivadas). Diccionario en `docs/Diccionario_de_datos_final.pdf`.
- **Limitaciones:** muestra no aleatoria y concentrada en ago-sep 2026; `fecha` puede no ser la de publicación; sin texto completo ni métricas de lectura.

## Equipo

| Integrante | Responsabilidad en la Parte II |
|---|---|
| Aguirre Milla, Fernando | Coordinación general, ingesta y descripción del origen de los datos (Parte I) |
| Toribio Arrieta, Josue Raul | Integración de metadatos y construcción de la base analítica (notebook 01) |
| Hurtado Vite, Mia Dayhana | Validaciones de calidad y pruebas estadísticas |
| Pacheco Vera, Fatima Isabella | Diccionario de datos, README y reproducibilidad del repositorio |
| Romano Castro, Aaron Adriano | Análisis visual, interpretación, redacción del informe y presentación |
