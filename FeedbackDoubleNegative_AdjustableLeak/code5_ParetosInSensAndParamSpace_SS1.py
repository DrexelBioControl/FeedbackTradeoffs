# For first steady state, plots Pareto fronts for each sensitivity pair and their points in parameter space
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data
data0 = np.load('Toggle_Paretos_Sens1_final.npz', allow_pickle=True)
data1 = np.load('Toggle_Paretos_Param1_final.npz', allow_pickle=True)
globals().update(data0)
globals().update(data1)

# Define pairs of sensitivity and parameter data
pairs = [
    (globals()[f"paretoset_Sens1Pair{i}_final"], globals()[f"paretoset_Sens1mask{i}_Param_final"])
    for i in range(1, 16)  # Adjust range based on the number of pairs
]

# Labels for each pair
labels_2d = [
    (r'$S_{\beta_x}(x_{ss})$', r'$S_{\beta_x}(y_{ss})$'),
    (r'$S_{\beta_x}(x_{ss})$', r'$S_{\beta_y}(x_{ss})$'),
    (r'$S_{\beta_x}(x_{ss})$', r'$S_{\beta_y}(y_{ss})$'),
    (r'$S_{\beta_x}(x_{ss})$', r'$S_{n}(x_{ss})$'),
    (r'$S_{\beta_x}(x_{ss})$', r'$S_{n}(y_{ss})$'),
    (r'$S_{\beta_x}(y_{ss})$', r'$S_{\beta_y}(x_{ss})$'),
    (r'$S_{\beta_x}(y_{ss})$', r'$S_{\beta_y}(y_{ss})$'),
    (r'$S_{\beta_x}(y_{ss})$', r'$S_{n}(x_{ss})$'),
    (r'$S_{\beta_x}(y_{ss})$', r'$S_{n}(y_{ss})$'),
    (r'$S_{\beta_y}(x_{ss})$', r'$S_{\beta_y}(y_{ss})$'),
    (r'$S_{\beta_y}(x_{ss})$', r'$S_{n}(x_{ss})$'),
    (r'$S_{\beta_y}(x_{ss})$', r'$S_{n}(y_{ss})$'),
    (r'$S_{\beta_y}(y_{ss})$', r'$S_{n}(x_{ss})$'),
    (r'$S_{\beta_y}(y_{ss})$', r'$S_{n}(y_{ss})$'),
    (r'$S_{n}(x_{ss})$', r'$S_{n}(y_{ss})$')
]

# Generate and save plots
for i, ((sens_data, param_data), (xlabel, ylabel)) in enumerate(zip(pairs, labels_2d), 1):
    fig, axes = plt.subplots(1, 2, figsize=(15, 7), constrained_layout=True)

    # 2D scatter plot
    axes[0].scatter(sens_data[:, 0], sens_data[:, 1], color='red', s=10)
    axes[0].set_xlabel(xlabel)
    axes[0].set_ylabel(ylabel)

    # 3D scatter plot
    ax_3d = fig.add_subplot(1, 2, 2, projection='3d')
    ax_3d.scatter(param_data[:, 0], param_data[:, 1], param_data[:, 2], color='red', s=10)
    ax_3d.set_xlabel(r'$\beta_x$')
    ax_3d.set_ylabel(r'$\beta_y$')
    ax_3d.set_zlabel(r'$n$')
    ax_3d.grid(True)

    # Set title and save
    fig.suptitle(
        f'Double Negative Feedback Steady State 1 L=0.1:\nPareto-Optimal Fronts and Parameters Pair {i}',
        fontsize=12, fontweight='bold'
    )
    plt.savefig(f'Toggle_Paretos_L0.1_Sens1Pair{i}_SS1.png', dpi=300)
    plt.close(fig)

