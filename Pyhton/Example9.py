import matplotlib.pyplot as plt
import numpy as np

# Define the function and the big-O bound
def f(x):
    return 3*x**2 + 8*x*np.log(x)

def big_o(x):
    return 10*x**2  # choosing 10 as a constant for illustrative purposes

# Generate a range of x values
x = np.linspace(1, 100, 400)
x = np.clip(x, 1, None)  # Avoid division by zero or log of zero

# Compute the function values and the big-O values
f_values = f(x)
big_o_values = big_o(x)

# Plotting the function and its Big-O bound
plt.figure(figsize=(10, 6))
plt.plot(x, f_values, label='3x^2 + 8x log(x)')
plt.plot(x, big_o_values, label='Big-O Bound (10x^2)', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function vs. Big-O Bound')
plt.legend()
plt.grid(True)
plt.show()
