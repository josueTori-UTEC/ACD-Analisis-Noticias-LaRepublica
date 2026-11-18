# Guion de exposición (15 min + 5 min de preguntas)

Todos los integrantes participan. Los tiempos suman 15 minutos.

| Diapositivas | Quién | Tiempo | Qué decir |
|---|---|---|---|
| 1–2 Portada, contexto y objetivos | Aguirre | 3 min | Qué datos había de la Parte I, qué problemas aparecieron (muestra no continua, fecha ambigua, sin texto) y por qué se reformuló el objetivo a «caracterizar la colección y medir sus sesgos». |
| 3–4 Pipeline y preprocesamiento | Toribio | 3,5 min | Las seis etapas y por qué CSV + SQLite. Cada tratamiento con su medición: 245 horas, 31 longitudes, 10 etiquetas, 40 atípicos conservados, 28→13 secciones y 408→54 etiquetas. Las tres variables nuevas que cambiaron los hallazgos. |
| 5–6 Sesgo temporal y fecha | Hurtado | 3 min | 43,4 % en ago-sep 2026; sección × año con V = 0,61. Fecha nunca anterior a la URL, 38,4 % difiere, hasta 1 632 días; no es zona horaria; 37 horas 00:00/05:00. |
| 7–8 Titulares, horarios y recomendaciones | Romano | 3 min | Comillas 45 % vs 10 %, cifras 94 % en Servicios, 51 % de Servicios en madrugada. Las cuatro recomendaciones. Son diferencias de estilo, no de audiencia. |
| 9 Conclusiones y repositorio | Pacheco | 2,5 min | Tres conclusiones, limitaciones, estructura del repo, diccionario final y los dos comandos para reproducir. Abre la ronda de preguntas. |

## Preguntas probables y cómo responderlas

1. **¿Por qué no eliminaron los atípicos?** Se revisaron: son titulares reales (notas breves o con declaraciones). La regla 1,5×IQR se usó como detector, no como criterio de borrado.
2. **¿Por qué agrupar secciones con menos de 20 noticias y etiquetas con menos de 5?** Con menos casos las comparaciones y las pruebas chi-cuadrado pierden validez (frecuencias esperadas menores que 5). Las columnas originales se conservan.
3. **¿Por qué Kruskal-Wallis y no ANOVA?** La longitud del titular no cumple normalidad ni varianzas parejas entre secciones. Kruskal-Wallis compara medianas sin esos supuestos.
4. **¿Por qué dicen que `fecha` puede ser de actualización?** Nunca es anterior a la fecha de la URL, y hay desfases de hasta 4,5 años que una zona horaria no explica. No se puede confirmar con estos datos; hay que validarla en el HTML.
5. **¿Los p-valores se pueden generalizar al diario?** No. La muestra no es aleatoria; describen asociaciones dentro de la colección. Por eso se reportan tamaños de efecto.
6. **¿Qué es el catálogo de áreas editoriales?** Una tabla propia del grupo que agrupa las 28 secciones en 6 áreas. No es una clasificación oficial del diario, y otra agrupación podría cambiar algunas comparaciones.
7. **¿Por qué SQLite?** El volumen es de 0,5 MB. SQLite es portable, no necesita servidor y permite consultas SQL.
8. **¿Qué pasa si hay nuevos datos?** Se reemplaza el CSV original y se ejecuta `python run_all.py`; las validaciones (`assert`) detienen el proceso si algo se rompe.
9. **¿Qué es `hnews`?** Un marcador que aparece en las URL desde 2025. Indica un cambio de formato; no se usa como categoría editorial.
10. **¿Qué mejorarían con más tiempo?** Recolectar con cuotas por mes y sección, capturar fecha de publicación y de actualización por separado, y analizar el texto de las noticias.
