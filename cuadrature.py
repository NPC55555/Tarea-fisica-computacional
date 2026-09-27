#!/usr/bin/env python3
from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    """
    Calcula los puntos de colocación y pesos de Gauss-Legendre en el intervalo [-1, 1].

    Args:
        N (int): Número de puntos de integración y pesos a calcular.

    Returns:
        tuple: Un par (x, w) de arreglos de NumPy con los puntos y pesos.
    """
    x, w = np.polynomial.legendre.leggauss(N)

    return x, w

def gaussxwab(a, b, x, w):
    """
    Escala los puntos de colocación y pesos desde el intervalo estándar [-1, 1] al intervalo [a, b].

    Args:
        a (float): Límite inferior de la integración.
        b (float): Límite superior de la integración.
        x (numpy.ndarray): Puntos de colocación originales.
        w (numpy.ndarray): Pesos originales.

    Returns:
        tuple: Puntos y pesos modificados linealmente al intervalo [a, b].
    """

    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def integrando(varInd):
    """
    Evalúa la función matemática objetivo de la integral.

    Ecuación: f(x) = x^6 - x^2 * sin(2x)

    Args:
        varInd (float o numpy.ndarray): Variable independiente a evaluar en la función.

    Returns:
        float o numpy.ndarray: Resultado de evaluar la variable en la función del integrando.
    """
    return varInd**6 - varInd**2 * np.sin(2 * varInd)

def pesos_puntos(N):
    """
    Devuelve de forma directa los pesos y puntos de colocación calculados para el valor N.

    Args:
        N (int): Número de puntos.

    Returns:
        tuple: Puntos y pesos devueltos por la función gaussxw.
    """
    return gaussxw(N)

def escalado(N, fun):
    """
    Realiza el escalado de los puntos y pesos específicamente para el intervalo de 1 a 3.

    Args:
        N (int): Número de puntos de colocación.
        fun (function): Función encargada de calcular los puntos y pesos originales.

    Returns:
        tuple: Puntos y pesos escalados de manera exacta al intervalo.
    """
    x, w = fun(N)
    return gaussxwab(1, 3, x, w)

def resultado(N, fun_escalado, fun_pesos):
    """
    Ejecuta la aproximación final de la cuadratura Gaussiana sumando los componentes ponderados.

    Args:
        N (int): Grado del polinomio o cantidad de puntos de evaluación.
        fun_escalado (function): Función encargada de realizar el mapeo de intervalo.
        fun_pesos (function): Función encargada de suministrar los pesos base.

    Returns:
        float: Resultado numérico de la aproximación de la integral definida.
    """
    x, w = fun_escalado(N, fun_pesos)
    return np.sum(w * integrando(x))

I2 = resultado(2, escalado, pesos_puntos)
I3 = resultado(3, escalado, pesos_puntos)
I4 = resultado(4, escalado, pesos_puntos)

print(I2)
print(I3)
print(I4)

