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

def init_bisection():
    func = input("Please enter your desired equation for root finding: y = ")
    while True:
        a = float(input("Please input the lower limit for finding the root: "))
        b = float(input("Please input the upper limit for finding the root: "))
        iterations = int(input("Enter the number of iterations: "))
        error_tolerance = float(input("Enter the max error tolerance: "))

        if (f(a, func) * f(b, func) < 0):
            bisection(func, a, b, iterations, error_tolerance)
            break
        else:
            print("Not a valid range! Try again")


def bisection(func, l, r, iterations, error_tolerance):
    cnt = 1
    prev_val = (l+r)/2.0
    xm = -1
    error = 0
    error_list = []
    Iteration_list = []
    Xu = []
    Xl = []
    Xm = []
    func_list = []
    ll = l
    rr = r

    while cnt <= iterations:
        cnt = cnt + 1
        xm = (l + r) / 2.0
        new_val = f(xm, func)

        Xl.append(l)
        Xu.append(r)
        Xm.append(xm)
        Iteration_list.append((cnt - 1))
        func_list.append(new_val)

        if (cnt == 2):
            error_list.append(np.nan)
        else:
            error = abs(xm - prev_val) / abs(xm * 1.00)
            error = error * 100.0
            error_list.append(error)

        prev_val = xm

        if (f(xm, func) * f(l, func)) < 0:
            r = xm
        else:
            l = xm

    data_table = pd.DataFrame(
        {"Iteration": Iteration_list, "Xl": Xl, "Xu": Xu, "Xm": Xm, "Error(%)": error_list, "f(Xm)": func_list})

    #data_table.set_index("Iteration")
    print(data_table)
    formatted_error = "{:.2f}".format(round(error, 2))
    print(f"Obtained root: {xm} with error {formatted_error}%")
    if (error > error_tolerance):
        print("Accuracy low due to iteration limitations!")

    x = []
    y = []
    if ll > rr:
        tmp = rr
        rr = ll
        ll = tmp
    while ll <= rr:
        x.append(ll)
        y.append(f(ll, func))
        ll = ll + 0.01

    x = np.array(x)
    y = np.array(y)
    plt.figure(figsize=(15, 15))
    plt.subplot(2, 1, 1)
    plt.xlabel("X")
    plt.ylabel("F(X)")
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.axvline(x=0.0, color='r')
    plt.plot(x, y)
    x = np.array(Iteration_list)
    y = np.array(error_list)
    plt.subplot(2, 1, 2)
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.axvline(x=0.0, color='r')
    plt.plot(x, y)
    plt.show()


