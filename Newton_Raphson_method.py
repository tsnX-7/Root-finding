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

def init_newton_raphson():
    func = input("Please enter your desired equation for root finding: y = ")
    while True:
        a = float(input("Please input the lower limit for finding the root: "))
        b = float(input("Please input the lower limit for finding the root: "))
        iterations = int(input("Enter the number of iterations: "))
        error_tolerance = float(input("Enter the max error tolerance: "))

        if (f(a, func) * f(b, func) < 0):
            first_derivative = str(Derivative(func).doit())
            if (abs(f(a, func)) < abs(f(b, func))):
                x0 = a
            else:
                x0 = b

            if (f(x0, first_derivative) != 0):
                newton_raphson(func, first_derivative, x0, iterations, error_tolerance)
                break
            else:
                print("Not a valid range! Try again")
        else:
            print("Not a valid range! Try again")


def newton_raphson(func, first_derivative, x0, iterations, error_tolerance):
    iteration_list = []
    prev_x = []
    xi_list = []
    error_list = []
    func_list = []
    cnt = 1
    xi = 1
    initial_guess = x0
    error = -1

    while cnt <= iterations:
        iteration_list.append(cnt)
        prev_x.append(x0)

        func_val = f(x0, func)
        first_derivative_val = f(x0, first_derivative)
        xi = x0 - (func_val / (first_derivative_val * 1.00))
        xi_list.append(xi)

        if (cnt == 1):
            error_list.append(np.NaN)
        else:
            error = (abs(x0 - xi) / abs(xi * 1.00)) * 100.0
            error_list.append(error)

        func_list.append(f(xi, func))
        cnt += 1
        x0 = xi

    data_table = pd.DataFrame(
        {"Iterations": iteration_list, "X(i-1)": prev_x, "Xi": xi_list, "Error(%)": error_list, "F(Xi)": func_list})

    print(data_table)
    formatted_error = "{:.2f}".format(round(error, 2))
    print(f"Obtained root: {xi} with error {formatted_error}%")
    if (error > error_tolerance):
        print("Accuracy low due to iteration limitations!")

    x = []
    y = []
    l = initial_guess - 12
    r = initial_guess + 12

    while l <= r:
        x.append(l)
        y.append(f(l, func))
        l += 0.01

    x = np.array(x)
    y = np.array(y)
    plt.figure(figsize=(15, 15))
    plt.subplot(2, 1, 1)
    plt.xlabel("X")
    plt.ylabel("F(X)")
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.axvline(x=0.0, color='r')
    plt.plot(x, y)
    x = np.array(list(data_table['Iterations']))
    y = np.array(list(data_table['Error(%)']))
    plt.subplot(2, 1, 2)
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.axvline(x=0.0, color='r')
    plt.plot(x, y)
    plt.show()