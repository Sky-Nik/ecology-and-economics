#!/usr/bin/env python -W ignore
import numpy as np

# матриця Леслі
L = np.array([
	[  0,   6, 15],
	[0.5,   0,  0],
	[  0, 0.5,  0]
])

# початковий розподіл популяції
x0 = np.array([1, 1, 1])

# розподіл через t = 5 кроків обчислюємо як L^t * x0
t = 5
print(f'x({t}) = {np.dot(np.linalg.matrix_power(L, t), x0)}')

# знаходимо власні значення і власні вектори
_lambda, x = np.linalg.eig(L)
# знаходимо найбільше додатне власне значення
lambda_L = np.max(_lambda)

print(f'lambda_L = {np.float_(lambda_L)}')

# знаходимо власний вектор що йому відповідає
x_L = x[:, _lambda == lambda_L].T[0] 
# нормуємо цей вектор в || ||_1 нормі
x_L /= np.linalg.norm(x_L, 1)

print(f'x_L = {np.abs(np.float_(x_L))}')

# знаходимо min t: ||x(t)||_1 > 75
t = 0
while np.sum(x0) <= 75:
	x0 = np.dot(L, x0)
	t += 1

print(f't = {t}, X({t}) = {np.sum(x0)}')
