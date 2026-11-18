"""Ejecuta el pipeline completo: preprocesamiento (notebook 01) y análisis (notebook 02).

Uso, desde la raíz del repositorio:
    python run_all.py

Regenera data/noticias_larepublica_final.csv, data/noticias_larepublica.db,
results/ y figures/ a partir de data/noticias_larepublica_original.csv.
"""
from pathlib import Path

import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parent
NOTEBOOKS = ['01_preprocesamiento.ipynb', '02_analisis_visualizacion.ipynb']

for nombre in NOTEBOOKS:
    ruta = RAIZ / 'notebooks' / nombre
    print(f'Ejecutando {nombre} ...')
    nb = nbformat.read(ruta, as_version=4)
    NotebookClient(nb, timeout=600, kernel_name='python3', resources={'metadata': {'path': str(ruta.parent)}}).execute()
    nbformat.write(nb, ruta)
    print('  listo')
print('Pipeline completo. Revisa data/, results/ y figures/.')
