# Tutorial de Uso y Resultados

Este script se puede ejecutar de forma directa en la terminal de su computadora. Al correr el archivo, el programa evalúa automáticamente la integral definida utilizando diferentes niveles de precisión (\(N = 2\), \(N = 3\) y \(N = 4\)).

## Resultados Obtenidos en la Terminal

Al ejecutar el comando `python cuadrature.py`, se despliegan de inmediato los siguientes resultados en consola:

*   **Para N = 2:** `306.8199344959197`
*   **Para N = 3:** `317.264151733829`
*   **Para N = 4:** `317.3453903341579`

### Análisis del Resultado Exacto
El resultado obtenido con **\(N = 4\)** es el valor **exacto** de la integral de la tarea, a excepción de los pequeños errores de redondeo o precisión decimal propios de la computadora.

---

## Flexibilidad y Modificación del Código

El script está diseñado de manera modular, lo que significa que el usuario puede editarlo fácilmente en su editor de texto para adaptarlo a otros problemas matemáticos:

*   **Cambiar el valor de N:** Puede modificar los argumentos de la función `resultado(N, ...)` en las líneas finales para probar cualquier otro número de puntos de colocación.
*   **Cambiar la función:** Si edita el bloque interno de la función `integrando(varInd)`, puede cambiar la ecuación actual por cualquier otra función matemática o integrales con potencias diferentes para obtener sus resultados numéricos al instante.

