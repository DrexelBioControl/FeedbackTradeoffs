
#  ---------------------------------------------------------------------
# |                                                                     |
# |                   PLOTTING UNIQUE SENSITIVITY PAIRS                 |
# |                     AND PARETO IN PARAMETER SPACE                   |
# |                                                                     |
#  ---------------------------------------------------------------------

# Python preliminary
import numpy as np
import matplotlib.pyplot as plt

# Load data
SenPolyhedrons = np.load('ARneg_SensitivityPolyhedrons.npy')
pareto_Sens = np.load('ARneg_SensitivityPareto.npy')
ParamPolyhedron = np.load('ARneg_ParamPolyhedron.npy', allow_pickle=True)
pareto_Params = np.load('ARneg_ParamPareto.npy', allow_pickle=True)


# _____________ Plot sensitivity pairs and Pareto front of each pair _____________

S_a_xss = SenPolyhedrons[:,0]
S_n_xss = SenPolyhedrons[:,1]

# ---------------------------------------------------------------


fig, axes = plt.subplots(1, 2, figsize=(8,4), constrained_layout=True)

axes[0].scatter(            S_a_xss,            S_n_xss,   color='orange', alpha= 0.5 , s=10)
axes[0].scatter(   pareto_Sens[:,0],   pareto_Sens[:,1],                              , s=10)
axes[0].set_xlabel(r'$S_{a}(x_{ss})$')
axes[0].set_ylabel(r'$S_{n}(x_{ss})$')

axes[1].scatter( ParamPolyhedron[:,0], ParamPolyhedron[:,1],   color='orange', alpha= 0.5 , s=10)
axes[1].scatter(   pareto_Params[:,0],   pareto_Params[:,1],                              , s=10)
axes[1].set_xlabel(r'$a$')
axes[1].set_ylabel(r'$n$')

fig.suptitle('Negative Autoregulation:\nPareto-Optimal Front and Parameters', fontsize=12, fontweight='bold')
plt.savefig('arneg_grantplot.png', dpi=300)
plt.show()
