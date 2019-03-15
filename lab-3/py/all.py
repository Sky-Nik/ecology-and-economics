#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np


def plt_setup():
	plt.legend()
	plt.grid(True)
	plt.get_current_fig_manager().full_screen_toggle() 
	plt.show()


df = pd.DataFrame({
	'price': [1.2, 1.7, 2.5, 2.9, 3.5, 4.2, 4.8, 5.5],
	'demand': [122, 97, 77, 56, 43, 36, 27, 17],
	'supply': [20, 35, 59, 65, 78, 83, 95, 120],
})

# Q P
plt.title('supply (price), demand (price)')
plt.plot(df['price'], df['demand'], 'r-', label='demand (price)')
plt.plot(df['price'], df['supply'], 'b--', label='supply (price)')
plt.xlabel('price')
plt.ylabel('supply, demand')
plt_setup()

# P Q
plt.plot(df['demand'], df['price'], 'r-', label='price (demand))')
plt.plot(df['supply'], df['price'], 'b--', label='price (supply))')
plt.xlabel('supply, demand')
plt.ylabel('price')
plt_setup()

price_space = np.arange(1.2, 5.5, 0.01)

df_interp = pd.DataFrame({
	'price': price_space,
	'demand': interp1d(df['price'], df['demand'], kind='cubic')(price_space),
	'supply': interp1d(df['price'], df['supply'], kind='cubic')(price_space),
})

# Q P
plt.title('Interpolated supply (price), demand (price)')
plt.plot(df_interp['price'], df_interp['demand'], 'r-', label='demand (price)')
plt.plot(df_interp['price'], df_interp['supply'], 'b--', label='supply (price)')
plt.xlabel('price')
plt.ylabel('suply, demand')
plt_setup()

# P Q
plt.plot(df_interp['demand'], df_interp['price'], 'r-', label='price (demand))')
plt.plot(df_interp['supply'], df_interp['price'], 'b--', label='price (supply))')
plt.xlabel('suply, demand')
plt.ylabel('price')
plt_setup()
