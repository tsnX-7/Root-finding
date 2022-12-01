import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp
from sympy import *
#from main import f

def f(x, func):
    val = eval(func)
    return val

def init_secant():
    func = input("Please enter your desired equation for root finding: y = ")
    while True:
        x0 = float(input("Please input the X(-1) guess for finding the root: "))
        x1 = float(input("Please input the X(0) guess for finding the root: "))
        iterations = int(input("Enter the number of iterations: "))
        error_tolerance = float(input("Enter the max error tolerance: "))

        if (f(x1, func) - f(x0, func) == 0):
            print("Division by zero error! Provide another guess ")
        else:
            secant(func, x0, x1, iterations, error_tolerance)
            break


def secant(func, x0, x1, iterations, error_tolerance):
    iteration_list = []
    Xi_prev = []
    Xi = []
    Xi_1 = []
    error_list = []
    func_list = []

    cnt = 1
    xi = 1

    while cnt <= iterations and x0!=x1:
        iteration_list.append(cnt)
        Xi_prev.append(x0)
        Xi.append(x1)

        try:
            xi = x1 - ((f(x1, func) * (x1 - x0)) / (f(x1, func) - f(x0, func)) * 1.00)
        except:
            print("Division By Zero error occured before completing iteration!")
            Xi_1.append(Xi_1[-1])
            error_list.append(error_list[-1])
            func_list.append(func_list[-1])
            break

        Xi_1.append(xi)

        x0 = x1
        x1 = xi

        if (cnt == 1):
            error_list.append(np.NaN)
        else:
            error = (abs(xi - x0) / abs(xi * 1.00)) * 100.0
            error_list.append(error)

        func_list.append(f(xi, func))
        cnt += 1

    data_table = pd.DataFrame(
        {"Iterations": iteration_list, "X(i-1)": Xi_prev, "X(i)": Xi, "X(i+1)": Xi_1, "Error(%)": error_list,
         "F(Xi)": func_list})

    print(data_table)

    formatted_error = "{:.2f}".format(round(error, 2))
    print(f"Obtained root: {xi} with error {formatted_error}%")
    if (error > error_tolerance):
        print("Accuracy low due to iteration limitations!")

    x = np.array(Xi_1)
    y = np.array(func_list)
    plt.figure(figsize=(15, 15))
    plt.subplot(2, 1, 1)
    plt.xlabel("X")
    plt.ylabel("F(X)")
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.axvline(x=0.0, color='r')
    plt.plot(x, y)
    x = np.array(iteration_list)
    y = np.array(error_list)
    plt.subplot(2, 1, 2)
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.axvline(x=0.0, color='r')
    plt.plot(x, y)
    plt.show()