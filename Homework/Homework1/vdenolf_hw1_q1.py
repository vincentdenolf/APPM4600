import numpy as np
import matplotlib.pyplot as plt

def p_coeff(x):
    return x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512

def p_factored(x):
    return (x-2)**9

x_arr = np.arange(1.920, 2.081, 0.001)

# for part (a)
plt.figure()
plt.plot(x_arr, p_coeff(x_arr), label='p_coeff(x)', color='blue')
plt.title(r"$p(x)$ Evaluated Using Coefficients")
plt.xlabel("x")
plt.ylabel("p(x)")

# for part (b)
plt.figure()
plt.plot(x_arr, p_factored(x_arr), label='p_factored(x)', color='orange')
plt.title(r"$p(x)$ Evaluated When Factored")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.show()

