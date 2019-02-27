#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

# проміжок на якому розглядається задачу, 12 місяців = 1 рік
t = np.linspace(0, 1, 1000)

# початкові умови
P10, P20 = 195, 90


# задаємо похідну dP / dt як функцію двох змінних: P і t
def dPdt(P, t):
	return 0.05 * P * (145 - P)


# знаходимо чисельні розв'язки відповідних задач Коші
P1, P2 = odeint(dPdt, P10, t), odeint(dPdt, P20, t)


# побудова графіків
matplotlib.rcParams.update({'font.size': 20})
plt.plot(t, P1, 'r-', label='$P(0) = 195$, numerical')
plt.plot(t, P2, 'b-', label='$P(0) = 90$, numerical')
plt.xlabel('$t$, місяців')
plt.ylabel("$P(t)$, особин хом'яків")
plt.legend()
plt.grid(True)
plt.get_current_fig_manager().full_screen_toggle() 
plt.show()
