import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import pandas as pd

x = sym.symbols('x')
sym.init_printing(use_unicode=True)

####### Exponential Function
f_eval_e = sym.exp(-x) - x
f_1_e = sym.exp(-x)
f_2_e = x
############# Trigonometric Function #####
f_eval_t = sym.sin(x**2) * x
f_1_t = sym.sin(x**2) - x
######################################

########## Polynomial Function #######
f_eval_p = x**2 - 5*x + 3  ## Roots at 0.7 and 4.3
f_1_p = (x**2 + 3) / 5
f_2_p = sym.sqrt(5*x - 3)
#############

p_i = 1
iterations = 100
tolerance = 0.001  ## is a value close to 0


def fixed_point_iteration(f_eval, f_1, tolerance, iterations, v_i):

    res = np.zeros((1, 5))
    res[0, 0] = 0
    res[0, 1] = v_i
    res[0, 2] = 0
    res[0, 3] = 100
    res[0, 4] = float(f_eval.subs(x, v_i))
    vv = 0.01  # 0.56714329  #0.7 
    ii = 0
    p_ant = v_i
    p_new = v_i
    while tolerance <= abs(float(f_eval.subs(x, p_new))) and ii <= iterations:
        p_new = float(f_1.subs(x, p_ant))
        ea = abs((p_new - p_ant) / p_new) * 100
        plt.scatter(p_ant, p_new, c='c')
        et = abs((vv - p_new) / vv) * 100
        p_ant = p_new
        ii += 1
        res = np.vstack((res, np.array([ii, p_new, ea, et, float(f_eval.subs(x, p_new))])))

    m = pd.DataFrame(res, columns=['i', 'x_i', 'ea', 'et', 'f(x)']).reset_index(drop=True)
    return m

print(fixed_point_iteration(f_eval_t, f_1_t, tolerance, iterations, p_i))
