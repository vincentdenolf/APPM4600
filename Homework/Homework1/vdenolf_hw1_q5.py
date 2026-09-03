import numpy as np
import matplotlib.pyplot as plt

delta = 10 ** np.linspace(-16, 0, 17)

def f(x , delta):
    return np.cos(x + delta) - np.cos(x)

def g(x, delta):
    return -2 * np.sin((2*x+delta)/2) * np.sin(delta/2)


# plotting first x-value
x1 = np.pi
diff1 = np.abs(g(x1, delta) - f(x1, delta))
plt.figure()
plt.loglog(delta, diff1)
plt.xlabel("Delta Values")
plt.ylabel("Absolute Difference in Expressions")
plt.title("Delta Versus Expression Differences for $x = \pi$")
plt.show()

# plotting second x-value
x2 = 10**6
diff2 = np.abs(g(x2, delta) - f(x2, delta))
plt.figure()
plt.loglog(delta, diff2)
plt.xlabel("Delta Values")
plt.ylabel("Absolute Difference in Expressions")
plt.title("Delta Versus Expression Differences for $x = 10^{6}$")
plt.show()

# now for the approximation in part (c)

def approx(x, delta):
    return -delta * np.sin(x) - ((delta**2)/2) * np.cos(x)

# reset x-vals just in case
x1 = np.pi
x2 = 10**6
diff3 = np.abs(approx(x1 , delta) - f(x1,delta))
plt.figure()
plt.loglog(delta, diff1, label = "Difference with Approximation from part (b)")
plt.loglog(delta, diff3, label = "Difference with My Approximation")
plt.xlabel("Delta Values")
plt.ylabel("Absolute Difference in Expressions")
plt.title("Delta Versus Expression Differences for $x = \pi$")
plt.legend()
plt.show()

diff4 = np.abs(approx(x2 , delta) - f(x2,delta))
plt.figure()
plt.loglog(delta, diff2, label = "Difference with Approximation from part (b)")
plt.loglog(delta, diff4, label = "Difference with My Approximation")
plt.xlabel("Delta Values")
plt.ylabel("Absolute Difference in Expressions")
plt.title("Delta Versus Expression Differences for $x = 10^6$")
plt.legend()
plt.show()

