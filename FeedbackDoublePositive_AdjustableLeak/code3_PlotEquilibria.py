# Plots equilibria coordinates of the two steady states both pre- and post- bifurcation

import numpy as np
import matplotlib.pyplot as plt

# Load data

data0 = np.load('dpos_SteadyStates_final.npz', allow_pickle=True)
for key, value in data0.items():
    globals()[key] = value

fig, axes = plt.subplots(1, 2, figsize=(8,4), constrained_layout=True)

axes[0].scatter(   xss1_final,   yss1_final,   s=10)
axes[0].set_xlabel(r'$x_{ss}$')
axes[0].set_ylabel(r'$y_{ss}$')
axes[0].set_title('Steady state 1')

axes[1].scatter(   xss2_final,   yss2_final,   s=10)
axes[1].set_xlabel(r'$x_{ss}$')
axes[1].set_ylabel(r'$y_{ss}$')
axes[1].set_title('Steady state 2')

fig.suptitle('Double Positive Feedback L= 1:\nEquilibria', fontsize=12, fontweight='bold')
plt.savefig('dpos_ParetosInSensAndParamSpaces_L1.png', dpi=300)
plt.show()
