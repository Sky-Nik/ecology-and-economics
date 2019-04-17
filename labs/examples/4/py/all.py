#!/usr/bin/env python
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit, minimize
from typing import Callable, Tuple


df = pd.DataFrame({
	'capital': [2_860, 2_740, 2_950, 2_880, 2_510, 2_690, 2_990, 2_850, 3_000, 3_070],
	'labor': [10_680, 10_310, 10_680, 10_800, 10_540, 10_420, 10_940, 10_710, 9_900, 9_930],
	'production': [49_920, 47_750, 50_550, 50_570, 47_820, 47_900, 51_900, 45_970, 48_030, 48_100],
})

df[[0, 1]] = df[['capital', 'labor']]


class ProductionFunction(object):
	def __init__(self, df: pd.DataFrame):
		self.A, self.a = curve_fit(
			lambda cl, A, a: A * cl['capital']**a * cl['labor']**(1 - a), 
			df[['capital','labor']], df['production']
		)[0]
	
	def __call__(self, cl) -> float:
		# cl[0] = cl['capital'], cl[1] = cl['labor']
		return self.A * cl[0]**self.a * cl[1]**(1 - self.a)

	def __repr__(self):
		return f'{self.A:.2f} * K^{self.a:.2f} * L^{1 - self.a:.2f}'


production_function = ProductionFunction(df)
print(production_function)

p, w_1, w_2 = 5, 2, 3


def cost(cl) -> float:
	# cl[0] = cl['capital'], cl[1] = cl['labor']
	return w_1 * cl[0] + w_2 * cl[1]


def profit(cl) -> float:
	return p * production_function(cl) - cost(cl)


def minus_profit(cl) -> float:
	return -profit(cl)


def minus_production_function(cl) -> float:
	return -production_function(cl)


# region limited cost, maximal profit
TC = 100_000

cl_star_1 = minimize(
	minus_profit, 
	x0=(10_000, 10_000), 
	constraints=(
		{'type': 'ineq', 'fun': lambda cl: cost(cl)},
		{'type': 'ineq', 'fun': lambda cl: TC - cost(cl)},
	)
)['x']

print(
	'limited cost, maximal profit:\n'
	f'	        cl_star  = {cl_star_1}\n'
	f'	   cost(cl_star) = {cost(cl_star_1)}\n'
	f'	product(cl_star) = {production_function(cl_star_1)}\n'
	f'	 profit(cl_star) = {profit(cl_star_1)}\n'
)
# enregion

# region limited cost, maximal production
cl_star_2 = minimize(
	minus_production_function, 
	x0=(10_000, 10_000), 
	constraints=(
		{'type': 'ineq', 'fun': lambda cl: cost(cl)},
		{'type': 'ineq', 'fun': lambda cl: TC - cost(cl)},
	)
)['x']

print(
	'limited cost, maximal production:\n'
	f'	        cl_star  = {cl_star_2}\n'
	f'	   cost(cl_star) = {cost(cl_star_2)}\n'
	f'	product(cl_star) = {production_function(cl_star_2)}\n'
	f'	 profit(cl_star) = {profit(cl_star_2)}\n'
)
# enregion

# region fixed production, minimal cost
q_0 = 55_000

cl_star_3 = minimize(
	cost, 
	x0=(10_000, 10_000), 
	constraints=(
		{'type': 'eq', 'fun': lambda cl: production_function(cl) - q_0},
	)
)['x']

print(
	'fixed production, minimal cost:\n'
	f'	        cl_star  = {cl_star_3}\n'
	f'	   cost(cl_star) = {cost(cl_star_3)}\n'
	f'	product(cl_star) = {production_function(cl_star_3)}\n'
	f'	 profit(cl_star) = {profit(cl_star_3)}\n'
)
# enregion