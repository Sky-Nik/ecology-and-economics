#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

t = np.linspace(0, 12, 1000)

P10 = 50
P20 = 300


def dPdt(P, t):
	return 0.004 * P * (150 - P)


matplotlib.rcParams.update({'font.size': 20})
plt.plot(t, odeint(dPdt, P10, t), 'r-', label='$P(0) = 50$, numerical')
plt.plot(t, odeint(dPdt, P20, t), 'b-', label='$P(0) = 300$, numerical')
plt.xlabel('$t$, місяців')
plt.ylabel('$P(t)$, особин кролів')
plt.legend()
plt.grid(True)
plt.get_current_fig_manager().full_screen_toggle() 
plt.show()
