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

x_values = [1, 2, 3]
y_values = [2, 4, 6]
x = 4
result = interpolation_polynomial(x_values, y_values, x)
print(result)
