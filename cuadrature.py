#!/usr/bin/env python3
from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)

    return x, w

def gaussxwab(a, b, x, w):

    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def integrando(varInd):
    return varInd**6 - varInd**2 * np.sin(2 * varInd)

def pesos_puntos(N):
    return gaussxw(N)

def escalado(N, fun):
    x, w = fun(N)
    return gaussxwab(1, 3, x, w)

def resultado(N, fun_escalado, fun_pesos):
    x, w = fun_escalado(N, fun_pesos)
    return np.sum(w * integrando(x))

I2 = resultado(2, escalado, pesos_puntos)
I3 = resultado(3, escalado, pesos_puntos)
I4 = resultado(4, escalado, pesos_puntos)

print(I2)
print(I3)
print(I4)
