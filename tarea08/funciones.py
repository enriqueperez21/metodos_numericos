import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt

def calcular_exponencial(exponente):
    return np.exp(exponente)

def log_natural(x):
    return np.log(x)

def sumatoria(a):
    return np.sum(a)

def grado2(x, y):
    # Sumatorias necesarias
    x_sum , y_sum , xy_sum , x2_sum = sumatoria(x), sumatoria(y), sumatoria(x * y), sumatoria(x ** 2) 
    # Número de puntos
    n = len(x)

    # Definimos las incógnitas
    b0, b1 = sp.symbols('b0 b1')

    # Definimos las dos ecuaciones basadas en la minimización de errores
    eq1 = sp.Eq(n * b0 + b1 * x_sum, y_sum)
    eq2 = sp.Eq(b0 * x_sum + b1 * x2_sum, xy_sum)

    # Resolvemos el sistema de ecuaciones
    solution = sp.solve((eq1, eq2), (b0, b1))
    b0,b1 = list(solution.values())
    def my_function(x): return (b0 + x*b1)
    return solution, my_function

def grado3(x, y):
    # Sumatorias necesarias
    x_sum , y_sum , xy_sum , x2_sum = sumatoria(x), sumatoria(y), sumatoria(x * y), sumatoria(x ** 2) 
    x3_sum, x4_sum, x2y_sum = sumatoria(x ** 3), sumatoria(x ** 4), sumatoria(x ** 2 * y) 

    # Número de puntos
    n = len(x)

    # Definimos las incógnitas
    a, b, c = sp.symbols('a b c')

    # Definimos las ecuaciones basadas en la minimización de errores
    eq1 = sp.Eq(a * x2_sum + b * x_sum + c * n, y_sum)
    eq2 = sp.Eq(a * x3_sum + b * x2_sum + c * x_sum, xy_sum)
    eq3 = sp.Eq(a * x4_sum + b * x3_sum + c * x2_sum, x2y_sum)

    # Resolvemos el sistema de ecuaciones
    solution = sp.solve((eq1, eq2, eq3), (a, b, c))
    a,b,c = list(solution.values())
    def my_function(x): return (a*x**2 + b*x + c)
    return solution, my_function

def grado4(x, y):
    # Sumatorias necesarias
    x_sum , y_sum , xy_sum , x2_sum = sumatoria(x), sumatoria(y), sumatoria(x * y), sumatoria(x ** 2) 
    x3_sum, x4_sum, x2y_sum = sumatoria(x ** 3), sumatoria(x ** 4), sumatoria(x ** 2 * y) 
    x5_sum, x6_sum, x3y_sum = sumatoria(x ** 5), sumatoria(x ** 6), sumatoria(x ** 3 * y)

    # Número de puntos
    n = len(x)

    # Definimos las incógnitas
    a, b, c, d = sp.symbols('a b c d')

    # Definimos las ecuaciones basadas en la minimización de errores
    eq1 = sp.Eq(a * x3_sum + b * x2_sum + c * x_sum + d * n, y_sum)
    eq2 = sp.Eq(a * x4_sum + b * x3_sum + c * x2_sum + d * x_sum,  xy_sum)
    eq3 = sp.Eq(a * x5_sum + b * x4_sum + c * x3_sum + d * x2_sum, x2y_sum)
    eq4 = sp.Eq(a * x6_sum + b * x5_sum + c * x4_sum + d * x3_sum, x3y_sum)

    # Resolvemos el sistema de ecuaciones
    solution = sp.solve((eq1, eq2, eq3, eq4), (a, b, c, d))
    a,b,c, d = list(solution.values())
    def my_function(x): return (a*x**3 + b*x**2 + c*x + d)
    return solution, my_function

def resolver_d(x, y):
    x_sum, x2_sum = sumatoria(x), sumatoria(x**2)
    Y_log = log_natural(y)
    Y_log_sum, XY_log_sum = sumatoria(Y_log), sumatoria(x*Y_log)
    # Número de puntos
    n = len(x)

    # Definimos las incógnitas
    B_log, a = sp.symbols('B_log a')

    # Definimos las dos ecuaciones basadas en la minimización de errores
    eq1 = sp.Eq(n * B_log + a * x_sum, Y_log_sum)
    eq2 = sp.Eq(B_log * x_sum + a * x2_sum, XY_log_sum)

    # Resolvemos el sistema de ecuaciones
    solution = sp.solve((eq1, eq2), (B_log, a))
    a = list(solution.values())
    b = float(a[0])
    a = float(a[1])
    b = np.exp(b)
    def my_function(x): return (b*np.exp(a*x))
    return {'a': a,'b':b}, my_function

def resolver_e(x, y):
    x_sum = sumatoria(x)
    Y_log = log_natural(y)
    X_log = log_natural(x)
    Y_log_sum, X_log_sum, XY_log_sum = sumatoria(Y_log), sumatoria(X_log), sumatoria(X_log*Y_log)
    X2_log_sum = sumatoria(X_log**2)
    # Número de puntos
    n = len(x)

    # Definimos las incógnitas
    B_log, a = sp.symbols('B_log a')

    # Definimos las dos ecuaciones basadas en la minimización de errores
    eq1 = sp.Eq(n * B_log + a * X_log_sum, Y_log_sum)
    eq2 = sp.Eq(B_log * X_log_sum + a * X2_log_sum, XY_log_sum)

    # Resolvemos el sistema de ecuaciones
    solution = sp.solve((eq1, eq2), (B_log, a))
    a = list(solution.values())
    b = float(a[0])
    a = float(a[1])
    b = np.exp(b)
    def my_function(x): return (b*x**a)
    return {'a': a,'b':b}, my_function

def plot_points_line(x, y, x_graph, y_graph):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(x, y, label='Datos originales')
    ax.plot(x_graph, y_graph, color='red', label='Datos predecidos')
    ax.legend()

def plot_points(x, y):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(x, y, label='Datos originales')
    ax.legend()
    pass