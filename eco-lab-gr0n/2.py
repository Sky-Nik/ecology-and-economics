#!/usr/bin/env python -W ignore
import numpy as np

# матриця Леслі
L = np.array([
	[  0,   9, 15],
	[1/3,   0,  0],
	[  0, 1/2,  0]
])

# початковий розподіл популяції
x0 = np.array([1, 0, 1])

# розподіл через t = 10 кроків обчислюємо як L^t * x0
t = 10
xt = np.dot(np.linalg.matrix_power(L, t), x0)
print(f'x({t}) = {xt}')  # x(10) = [4864.875       781.45833333  191.625     ]

# знаходимо власні значення і власні вектори
_lambda, x = np.linalg.eig(L)
# знаходимо найбільше додатне власне значення
lambda_L = np.max(_lambda)

print(f'lambda_L = {np.float_(lambda_L)}')  # lambda_L = 2.0536215758789726

# знаходимо власний вектор що йому відповідає
x_L = x[:, _lambda == lambda_L].T[0] 
# нормуємо цей вектор в || ||_1 нормі
x_L /= np.linalg.norm(x_L, 1)

print(f'x_L = {np.abs(np.float_(x_L))}')  # x_L = [0.83206163 0.13505598 0.03288239]

# знаходимо min t: ||x(t)||_1 > 90
t = 0
while np.sum(x0) <= 90:
	x0 = np.dot(L, x0)
	t += 1

print(f't = {t}, X({t}) = {np.sum(x0)}')  # t = 5, X(5) = 173.41666666666666
