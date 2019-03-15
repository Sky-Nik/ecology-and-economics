#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
from typing import Callable

df = pd.DataFrame({
	'price': [1.2, 1.7, 2.5, 2.9, 3.5, 4.2, 4.8, 5.5],
	'demand': [122, 97, 77, 56, 43, 36, 27, 17],
	'supply': [20, 35, 59, 65, 78, 83, 95, 120],
})


class DemandLin(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a * t + b, 
			df['price'], df['demand'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a * t + self.b


class SupplyLin(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a * t + b, 
			df['price'], df['supply'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a * t + self.b


df_lin = pd.DataFrame({
	'price': df['price'],
	'demand': DemandLin(df)(df['price']),
	'supply': SupplyLin(df)(df['price']),
})


class DemandExp(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a * np.exp(b * t), 
			df['price'], df['demand'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a * np.exp(self.b * t)


class SupplyExp(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a * np.exp(b * t), 
			df['price'], df['supply'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a * np.exp(self.b * t)


df_exp = pd.DataFrame({
	'price': df['price'],
	'demand': DemandExp(df)(df['price']),
	'supply': SupplyExp(df)(df['price']),
})


class DemandLog(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a + b * np.log(t), 
			df['price'], df['demand'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a + self.b * np.log(t)


class SupplyLog(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a + b * np.log(t), 
			df['price'], df['supply'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a + self.b * np.log(t)


df_log = pd.DataFrame({
	'price': df['price'],
	'demand': DemandLog(df)(df['price']),
	'supply': SupplyLog(df)(df['price']),
})

print(
	f"ERROR [demand, lin]: {np.sum((df['demand'] - df_lin['demand'])**2)}\n"
	f"ERROR [supply, lin]: {np.sum((df['supply'] - df_lin['supply'])**2)}\n"
	f"ERROR [demand, exp]: {np.sum((df['demand'] - df_exp['demand'])**2)}\n"
	f"ERROR [supply, exp]: {np.sum((df['supply'] - df_exp['supply'])**2)}\n"
	f"ERROR [demand, log]: {np.sum((df['demand'] - df_log['demand'])**2)}\n"
	f"ERROR [supply, log]: {np.sum((df['supply'] - df_log['supply'])**2)}"
)


# P Q
plt.plot(df['price'], df['demand'], 'r-', label='demand, true')
plt.plot(df['price'], df['supply'], 'b-', label='supply, true')
plt.plot(df_lin['price'], df_lin['supply'], 'b--', label='supply, lin')
plt.plot(df_exp['price'], df_exp['demand'], 'r-.', label='demand, exp')
plt.title('True and interpolated supply and demand', fontsize=20)
plt.xlabel('$P$', fontsize=16)
plt.ylabel('$Q$', fontsize=16)
plt.legend()
plt.grid(True)
plt.get_current_fig_manager().full_screen_toggle() 
plt.show()


# Q P
plt.plot(df['demand'], df['price'], 'r-', label='demand, true')
plt.plot(df['supply'], df['price'], 'b-', label='supply, true')
plt.plot(df_lin['supply'], df_lin['price'], 'b--', label='supply, lin')
plt.plot(df_exp['demand'], df_exp['price'], 'r-.', label='demand, exp')
plt.title('True and interpolated supply and demand', fontsize=20)
plt.xlabel('$Q$', fontsize=16)
plt.ylabel('$P$', fontsize=16)
plt.legend()
plt.grid(True)
plt.get_current_fig_manager().full_screen_toggle() 
plt.show()
