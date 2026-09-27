
# Tutorial de Uso

Este tutorial práctico le guiará en el proceso de utilización del script para aproximar la integral definida mediante el método numérico de cuadratura Gaussiana.

## Requisitos Previos

Antes de ejecutar el script, asegúrese de tener instaladas las dependencias científicas requeridas en su entorno de Python:

```bash
pip install numpy scipy matplotlib
```

## Guía de Ejecución Rápida

### Opción 1: Ejecutar desde la terminal
Puede clonar el repositorio y correr de manera directa el script principal para observar las aproximaciones numéricas según el valor de N:

```bash
python cuadrature.py
```

### Opción 2: Importar las funciones en un script propio
Si desea utilizar la lógica de aproximación en otro bloque de código o en un cuaderno de Jupyter Notebook, puede importar el módulo de la siguiente manera:

```python
from cuadrature import resultado, escalado, pesos_puntos

# Definir el grado de precisión deseado (N)
puntos_evaluacion = 4

# Calcular la aproximación de la integral
mi_integral = resultado(puntos_evaluacion, escalado, pesos_puntos)

print(f"El resultado calculado para la aproximación es: {mi_integral}")
```
