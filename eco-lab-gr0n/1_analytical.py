#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 1000)


def P(t, c):
    return 145 * np.exp(7.25 * t) / (np.exp(7.25 * t) + c)


def P1(t):
    return P(t, - 10 / 39)


def P2(t):
    return P(t, 11 / 18)


matplotlib.rcParams.update({'font.size': 20})
plt.plot(t, P1(t), 'r-', label='$P(0) = 195$, analytical')
plt.plot(t, P2(t), 'b-', label='$P(0) = 90$, analytical')
plt.xlabel('$t$, місяців')
plt.ylabel("'$P(t)$, особин хом'яків")
plt.legend()
plt.grid(True)
plt.get_current_fig_manager().full_screen_toggle() 
plt.show()
