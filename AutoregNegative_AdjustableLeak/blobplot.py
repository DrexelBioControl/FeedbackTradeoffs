
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
SenPolyhedrons_L0 = np.load('ARneg_SensitivityPolyhedrons_L0.npy')
pareto_Sens_L0 = np.load('ARneg_SensitivityPareto_L0.npy')
ParamPolyhedron_L0 = np.load('ARneg_ParamPolyhedron_L0.npy', allow_pickle=True)
pareto_Params_L0 = np.load('ARneg_ParamPareto_L0.npy', allow_pickle=True)

SenPolyhedrons_L01 = np.load('ARneg_SensitivityPolyhedrons_L0.1.npy')
pareto_Sens_L01 = np.load('ARneg_SensitivityPareto_L0.1.npy')
ParamPolyhedron_L01 = np.load('ARneg_ParamPolyhedron_L0.1.npy', allow_pickle=True)
pareto_Params_L01 = np.load('ARneg_ParamPareto_L0.1.npy', allow_pickle=True)

SenPolyhedrons_L1 = np.load('ARneg_SensitivityPolyhedrons_L1.npy')
pareto_Sens_L1 = np.load('ARneg_SensitivityPareto_L1.npy')
ParamPolyhedron_L1 = np.load('ARneg_ParamPolyhedron_L1.npy', allow_pickle=True)
pareto_Params_L1 = np.load('ARneg_ParamPareto_L1.npy', allow_pickle=True)

SenPolyhedrons_L10 = np.load('ARneg_SensitivityPolyhedrons_L10.npy')
pareto_Sens_L10 = np.load('ARneg_SensitivityPareto_L10.npy')
ParamPolyhedron_L10 = np.load('ARneg_ParamPolyhedron_L10.npy', allow_pickle=True)
pareto_Params_L10 = np.load('ARneg_ParamPareto_L10.npy', allow_pickle=True)


# _____________ Plot sensitivity pairs and Pareto front of each pair _____________

S_a_xss_L0 = SenPolyhedrons_L0[:,0]
S_n_xss_L0 = SenPolyhedrons_L0[:,1]

S_a_xss_L01 = SenPolyhedrons_L01[:,0]
S_n_xss_L01 = SenPolyhedrons_L01[:,1]

S_a_xss_L1 = SenPolyhedrons_L1[:,0]
S_n_xss_L1 = SenPolyhedrons_L1[:,1]

S_a_xss_L10 = SenPolyhedrons_L10[:,0]
S_n_xss_L10 = SenPolyhedrons_L10[:,1]

# ---------------------------------------------------------------


fig, axes = plt.subplots(1, 2, figsize=(6,3), constrained_layout=True)

axes[0].scatter(            S_a_xss_L0,            S_n_xss_L0,   alpha= 0.5 , s=5, color='cornflowerblue')
axes[0].scatter(            S_a_xss_L01,            S_n_xss_L01,   alpha= 0.5 , s=5, color='bisque')
axes[0].scatter(            S_a_xss_L1,            S_n_xss_L1,   alpha= 0.5 , s=5, color='palegreen')
axes[0].scatter(            S_a_xss_L10,            S_n_xss_L10,   alpha= 0.5 , s=5, color='lightcoral')
axes[0].scatter(   pareto_Sens_L0[:,0],   pareto_Sens_L0[:,1],                s=5, color='blue')
axes[0].scatter(   pareto_Sens_L01[:,0],   pareto_Sens_L01[:,1],                s=5, color='orange')
axes[0].scatter(   pareto_Sens_L1[:,0],   pareto_Sens_L1[:,1],                s=5, color='green')
axes[0].scatter(   pareto_Sens_L10[:,0],   pareto_Sens_L10[:,1],                s=5, color='red')
axes[0].set_xlabel(r'$|S_{a}(x_{ss})|$')
axes[0].set_ylabel(r'$|S_{n}(x_{ss})|$')
axes[0].set_xlim(-0.01, 0.4)
axes[0].set_ylim(-0.01, 0.4)


axes[1].scatter(   pareto_Params_L0[:,0],   pareto_Params_L0[:,1]                               , s=5, color='blue')
axes[1].scatter(   pareto_Params_L01[:,0],   pareto_Params_L01[:,1]                               , s=5, color='orange')
axes[1].scatter(   pareto_Params_L1[:,0],   pareto_Params_L1[:,1]                               , s=5, color='green')
axes[1].scatter(   pareto_Params_L10[:,0],   pareto_Params_L10[:,1]                               , s=5, color='red')
axes[1].set_xlabel(r'$a$')
axes[1].set_ylabel(r'$n$')
axes[1].set_xlim(-0.05, 6)
axes[1].set_ylim(9, 10.1)

fig.suptitle('Negative Autoregulation:\nPareto-Optimal Front and Parameters', fontsize=12, fontweight='bold')
plt.savefig('arneg_grantplot.png', dpi=300)
