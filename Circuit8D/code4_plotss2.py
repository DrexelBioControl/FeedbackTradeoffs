import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data
data0 = np.load('circuit1_Paretos_Sens2_final.npz', allow_pickle=True)
data1 = np.load('circuit1_Paretos_Param2_final.npz', allow_pickle=True)

globals().update(data0)
globals().update(data1)

# Define pairs of sensitivity and parameter data
pairs = [
    (
        data0[f"paretoset_Sens2Pair{i}_final"],
        data1[f"paretoset_Sens2mask{i}_Param_final"]
    )
    for i in range(1, 16)
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
for i, ((sens_data_pareto, param_data), (xlabel, ylabel)) in enumerate(zip(pairs, labels_2d), 1):
    # Create figure and subplots
    fig = plt.figure(figsize=(8, 4))  # Adjust figure size

    # 2D scatter plot
    ax2d = fig.add_subplot(1, 2, 1)
    ax2d.scatter(sens_data_pareto[:, 0], sens_data_pareto[:, 1], s=10)
    ax2d.set_xlabel(xlabel)
    ax2d.set_ylabel(ylabel)

    # 3D scatter plot
    ax_3d = fig.add_subplot(1, 2, 2, projection='3d')
    ax_3d.scatter(param_data[:, 0], param_data[:, 1], param_data[:, 2], s=10)
    ax_3d.set_xlabel(r'$\beta_x$')
    ax_3d.set_ylabel(r'$\beta_y$')
    ax_3d.set_zlabel(r'$n$')
    ax_3d.grid(True)
    ax_3d.set_box_aspect([1, 1, 1])  # Equal aspect ratio for 3D plot

    # Reduce tick density on 3D axes
    ax_3d.locator_params(nbins=5, axis='x')  # X-axis: 5 ticks
    ax_3d.locator_params(nbins=5, axis='y')  # Y-axis: 5 ticks
    ax_3d.locator_params(nbins=4, axis='z')  # Z-axis: 4 ticks

    # Adjust layout
    fig.tight_layout(pad=2.5)  # Adjust padding between subplots

    # Set title and save
    fig.suptitle(
        f'Steady State 2:\nPareto-Optimal Fronts and Parameters Pair {i}',
        fontsize=10, fontweight='bold'
    )
    plt.savefig(f'Paretos_Sens2Pair{i}_SS2.png', dpi=300)
    plt.close(fig)

