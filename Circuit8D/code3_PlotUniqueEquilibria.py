import numpy as np
import matplotlib.pyplot as plt

# Load data
data0 = np.load('circuit1_SteadyStates_final.npz', allow_pickle=True)
for key, value in data0.items():
    globals()[key] = value

# Combine x and y coordinates
coords_ss1 = np.column_stack((xss1_final, yss1_final))
coords_ss2 = np.column_stack((xss2_final, yss2_final))

# Find unique points in each set by excluding points that exist in the other
unique_ss1 = np.array([point for point in coords_ss1 if point.tolist() not in coords_ss2.tolist()])
unique_ss2 = np.array([point for point in coords_ss2 if point.tolist() not in coords_ss1.tolist()])

fig, axes = plt.subplots(1, 2, figsize=(8, 4), constrained_layout=True)

# Plot unique points for steady state 1
axes[0].scatter(unique_ss1[:, 0], unique_ss1[:, 1], s=10)
axes[0].set_xlabel(r'$x_{ss}$')
axes[0].set_ylabel(r'$y_{ss}$')
axes[0].set_title('Steady state 1')

# Plot unique points for steady state 2
axes[1].scatter(unique_ss2[:, 0], unique_ss2[:, 1], s=10)
axes[1].set_xlabel(r'$x_{ss}$')
axes[1].set_ylabel(r'$y_{ss}$')
axes[1].set_title('Steady state 2')

fig.suptitle('Circuit 1: Unique Equilibria', fontsize=12, fontweight='bold')
plt.savefig('circuit1_UniqueEquilibria.png', dpi=300)
plt.show()

