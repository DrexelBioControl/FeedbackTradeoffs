# For first steady state, plots Pareto fronts for each sensitivity pair and their points in parameter space
import numpy as np
import matplotlib.pyplot as plt



# Load data corresponding to steady state xss1

data0 = np.load('arpos_Paretos_Sens1_final.npz', allow_pickle=True)
for key, value in data0.items():
    globals()[key] = value
    
data1 = np.load('arpos_Paretos_Param1_final.npz', allow_pickle=True)
for key, value in data1.items():
    globals()[key] = value
    
# Load data corresponding to steady state xss2
    
data2 = np.load('arpos_Paretos_Sens2_final.npz', allow_pickle=True)
for key, value in data2.items():
    globals()[key] = value
    
data3 = np.load('arpos_Paretos_Param2_final.npz', allow_pickle=True)
for key, value in data3.items():
    globals()[key] = value


fig, axes = plt.subplots(2, 2, figsize=(7, 7), constrained_layout=True)

axes[0,0].scatter(   paretoset_Sens1Pair1_final[:,0],   paretoset_Sens1Pair1_final[:,1],   s=10)
axes[0,0].set_title('Steady state 1')
#axes[0,0].set_xlabel(r'$S_{\alpha}(x_{ss})$')
axes[0,0].set_ylabel(r'$S_{n}(y_{ss})$')

axes[0,1].scatter(   paretoset_Sens1mask1_Param_final[:,0],   paretoset_Sens1mask1_Param_final[:,1],   s=10)
axes[0,1].set_title('Steady state 1')
#axes[0,1].set_xlabel(r'$\alpha$')
axes[0,1].set_ylabel(r'$n$')

axes[1,0].scatter(   paretoset_Sens2Pair1_final[:,0],   paretoset_Sens2Pair1_final[:,1],   s=10)
axes[1,0].set_title('Steady state 2')
axes[1,0].set_xlabel(r'$S_{\alpha}(x_{ss})$')
axes[1,0].set_ylabel(r'$S_{n}(y_{ss})$')

axes[1,1].scatter(   paretoset_Sens2mask1_Param_final[:,0],   paretoset_Sens2mask1_Param_final[:,1],   s=10)
axes[1,1].set_title('Steady state 2')
axes[1,1].set_xlabel(r'$\alpha$')
axes[1,1].set_ylabel(r'$n$')

# Add a global title
fig.suptitle('Positive Autoregulation L=0:\nPareto-Optimal Fronts and Parameters', fontsize=16, fontweight='bold')
plt.savefig('arpos_ParetosInSensAndParamSpaces_L0.png', dpi=300)
plt.show()

