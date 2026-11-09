# Análisis de patrones de cobertura periodística en La República

**Curso:** DS3021 Análisis Computacional de Datos  
**Equipo:** Grupo 3 — UTEC, 2026

## Propósito

Caracterizar la colección de noticias de La República por secciones, etiquetas, autores, horarios registrados y características de los titulares. Los resultados describen una muestra de 1 116 registros y no representan un censo de todas las publicaciones del medio.

## Equipo

- Aguirre Milla, Fernando
- Toribio Arrieta, Josue Raul
- Hurtado Vite, Mia Dayhana
- Pacheco Vera, Fatima Isabella
- Romano Castro, Aaron Adriano

## Archivos

```text
ACD-Grupo3/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── noticias_larepublica_original.csv
│   └── noticias_larepublica_final.csv
├── notebooks/
│   ├── 01_preprocesamiento.ipynb
│   └── 02_analisis_visualizacion.ipynb
├── docs/
│   ├── Diccionario_de_datos_original.pdf
│   ├── Diccionario_de_datos_final.pdf
│   └── Diccionario_de_datos_final.docx
├── results/
│   ├── indicadores.json
│   ├── resumen_secciones.csv
│   └── resumen_autores.csv
├── figures/
│   └── 01_secciones.png ... 08_dias_semana.png
├── reports/
│   ├── Informe_final_ACD_Grupo3.pdf
│   └── Informe_final_ACD_Grupo3.docx
└── presentacion/
    ├── Presentacion_ACD_Grupo3.pptx
    ├── Presentacion_ACD_Grupo3.pdf
    └── Guion_de_exposicion.md
```

## Reproducción del análisis

Se requiere Python 3.10 o posterior. Desde la raíz del repositorio:

```bash
pip install -r requirements.txt
jupyter notebook
```

En Jupyter, abrir `notebooks/01_preprocesamiento.ipynb` y seleccionar **Run All**. Esta ejecución lee el archivo original de `data/`, construye las variables, exporta el CSV final y guarda los indicadores en `results/`. Luego abrir `notebooks/02_analisis_visualizacion.ipynb` y seleccionar **Run All** para obtener las tablas y regenerar los ocho gráficos en `figures/`.

**Todo el código se encuentra dentro de los dos notebooks `.ipynb`**. No se necesitan scripts Python externos ni acceso a internet para reproducir los resultados usando el CSV incluido. Los notebooks contienen las celdas ejecutadas y sus salidas.

Los archivos también se pueden abrir desde la raíz mediante Jupyter, porque cada notebook identifica el directorio `data/` antes de procesar.

## Preparación de datos

1. Comprobación de las siete columnas originales y normalización de los campos textuales.
2. Detección de URL duplicadas y verificación de identificadores y títulos no vacíos.
3. Conservación explícita de las diez etiquetas ausentes mediante la categoría `Sin etiqueta`.
4. Cálculo de la longitud del titular a partir del texto normalizado.
5. Asociación de la sección con el primer segmento de la URL y contraste de fechas sin sustituirlas.
6. Construcción de atributos temporales, indicadores del titular y agrupaciones descriptivas.
7. Exportación del CSV de 18 columnas, indicadores, tablas y ocho gráficos.

Se conservaron las observaciones con longitudes atípicas del titular; la regla IQR se usó como detector, no como criterio automático de exclusión. Las fechas incorporadas en las rutas de URL no se consideran equivalentes a la fecha de publicación.

## Resultados y limitaciones

El CSV de origen tiene 1 116 filas y 7 columnas. El CSV final mantiene las 1 116 filas y contiene 18 variables. Las URL son únicas y las variables finales no presentan datos faltantes. La validación está integrada en el notebook de preprocesamiento. Los resultados completos están en `results/indicadores.json`.

La selección de noticias no es probabilística y no cubre todos los días del periodo. `tag` y `seccion` son niveles diferentes de clasificación. No se dispone del texto completo de las noticias, métricas de audiencia ni historial de actualización de los artículos. La colección no permite inferir por sí sola tendencias temporales generales de la redacción.

## Fuente

Datos recopilados de páginas públicas de [La República](https://larepublica.pe/). Las URL originales están disponibles en `data/noticias_larepublica_original.csv`.
