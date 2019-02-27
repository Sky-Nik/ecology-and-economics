#!/usr/bin/env python -W ignore
import numpy as np

L = np.array([
	[  0,   6, 15],
	[0.5,   0,  0],
	[  0, 0.5,  0]
])

x0 = np.array([1, 1, 1])

print(f'x(5) = {np.dot(np.linalg.matrix_power(L, 5), x0)}')

λ, x = np.linalg.eig(L)

λ_L = np.max(λ)

print(f'λ_L = {np.float_(λ_L)}')

x_L = x[:, λ == λ_L].T[0] 

x_L /= np.linalg.norm(x_L, 1)

print(f'x_L = {np.abs(np.float_(x_L))}')

t = 0
while np.sum(x0) <= 75:
	x0 = np.dot(L, x0)
	t += 1

print(f't = {t}, X({t}) = {np.sum(x0)}')
