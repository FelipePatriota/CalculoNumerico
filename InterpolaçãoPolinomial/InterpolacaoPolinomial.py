import numpy as np

def interpolation_polynomial(x_values, y_values, x):
    n = len(x_values)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i][j] = x_values[i]**(n-j-1)
    b = y_values
    coefficients = np.linalg.solve(A, b)
    result = 0
    for i, coefficient in enumerate(coefficients):
        result += coefficient * x**(n-i-1)
    return result

x_values = [20, 25, 30, 35, 40, 45, 50]
y_values = [0.99907, 0.99852, 0.99826, 0.99818, 0.99828, 0.99849, 0.99878]
x = 4
result = interpolation_polynomial(x_values, y_values, x)
print(result)
