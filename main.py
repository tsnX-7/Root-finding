import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp

from sympy import *
from Bisection_method import init_bisection
from False_Position_method import init_false_position
from Newton_Raphson_method import init_newton_raphson
from Secant_method import init_secant

def f(x, func):
    val = eval(func)
    return val

print("Select a method for root finding: ")
print("1. Bisection")
print("2. False Position")
print("3. Newton Raphson")
print("4. Secant")

selection = int(input("Your selection: "))

if selection == 1:
    init_bisection()
elif selection == 2:
    init_false_position()
elif selection == 3:
    init_newton_raphson()
elif selection == 4:
    init_secant()
else:
    raise Exception('Input Error')
