This repository contains the following folders and files. For folders in which there are code files, these files should be executed in the order listed.


-----------------------------------------


- SensitivityFunctionDerivation:
  This folder contains all Mathematica notebooks deriving the sensitivity functions of our three dual-species feedback circuits: positive-negative feedback, double-positive feedback and double-negative feedback (toggle switch). 


-----------------------------------------


- SensitivityFunctionDerivation_WithLeak:
  This folder contains all Mathematica notebooks deriving the sensitivity functions of our five feedback circuits with leak mechanism considered: positive autoregulation, negative autoregulation, positive-negative feedback, double-positive feedback and double-negative feedback (toggle switch). 
  

-----------------------------------------


- AutoregulationNegative_AdjustableLeak: 
  Sensitivity analysis of negative autoregulation circuit.

- - codeI_arneg_optimisedsolve.py:
    This file defines the negative autoregualtion system (dynamical equations, sensitivity functions) and sets up the grid search. The grid search is performed over two paramters: alpha and n. 
    
- - codeII_bashscript.sh:
    Run this in terminal to execute codeI_arneg_optimisedsolve.py

- - codeIII_arneg_combine.py:
    Since codeI_arneg_optimisedsolve.py outputs separate files for each alpha value, indexed by 'aindex', run this file to combine all individual outputs.

- - codeIV_ParetosInSensAndParamSpace.py:


- - blobplot.py:
    Should the reader wish to recreate the plots in Figure 5 (we call these "blobplots"), the reader should rerun codeI to codeIV for leak levels: 0, 0.1, 1 and 10; and name the corresponding output data with suffix "_L{leak level}". That is, for leak level 0.1, use naming convention: "ARneg_SensitivityPolyhedrons_L0.1.npy". Run this codeV file in the end to generate plot. 


-----------------------------------------


- AutoregulationPositive_AdjustableLeak: 
  Sensitivity analysis of positive autoregulation circuit.

- - codeI_OptimisedSolve.py: 
    This file outputs 

- - codeII_Plots.py: 

- - codeIII_blobplot.py: 

- - blobplot.py:
    Should the reader wish to recreate the plots in Figure 5 (we call these "blobplots"), the reader should rerun codeI to codeIV for leak levels: 0, 0.1, 1 and 10; and name the corresponding output data with suffix "_L{leak level}". That is, for leak level 0.1, use naming convention: "ARneg_SensitivityPolyhedrons_L0.1.npy". Run this codeV file in the end to generate plot. 


-----------------------------------------


- FeedbackPositiveNegative_AdjustableLeak: 
  Sensitivity analysis of positive-negative feedback loop. The user is able to tweak the model leak level in codeI_posneg_optimisedsolve.py.

- - code1_posneg_optimisedsolve.py:
    This file defines the positive-negative feedback system and sets up the grid search. The grid search is performed over three parameters: beta_x, beta_y, n. For each beta_x, indexed by 'betaindex', a full sweep is performed on beta_y and n. Each full sweep outputs a single set of steady states in file 'posneg_steadystates' + str(betaindex) + '.npz'. For each steady state set, their corresponding Pareto fronts are contained in output files 'posneg_Paretos_Sens1' + str(betaindex) + '.npz'. The respective paramter combinations of these Pareto fronts are contained in output file 'posneg_Paretos_Params1' + str(betaindex) + '.npz'.

- - submit.sh:
    Run this in terminal to execute code1_posneg_optimisedsolve.py

- - code2_posneg_combine.py:
    Since codeI_posneg_optimisedsolve.py outputs separate files for each beta_x value, indexed by 'betaindex', run this file to combine all individual outputs. The corresponding new combined files will be named with '_final': 'Toggle_SteadyStates_final.npz', 'Toggle_Paretos_Sens1_final.npz', 'Toggle_Paretos_Param1_final.npz'. 

- - code3_ParetosInSensAndParamSpace_SS1.py:
    Execute this to plot Pareto fronts and their parameter values.


-----------------------------------------


- FeedbackDoubleNegative_AdjustableLeak: 
  Sensitivity analysis of double-negative feedback loop (toggle switch). The user is able to tweak the model leak level in codeI_negneg_optimisedsolve.py.

- - codeI_negneg_optimisedsolve.py: 
    This file defines the toggle switch system and sets up the grid search. The grid search is performed over three parameters: beta_x, beta_y, n. For each beta_x, indexed by 'betaindex', a full sweep is performed on beta_y and n. Each full sweep outputs the two sets of steady states in file 'Toggle_steadystates' + str(betaindex) + '.npz'. For each of the two steady states, their corresponding Pareto fronts are contained in output files: 'Toggle_Paretos_Sens1' + str(betaindex) + '.npz' and 'Toggle_Paretos_Sens2' + str(betaindex) + '.npz' respectively. The respective paramter combinatiosn of these pareto fronts are contained in output files: 'Toggle_Paretos_Params1' + str(betaindex) + '.npz' and 'Toggle_Paretos_Params2' + str(betaindex) + '.npz'.

- - submit.sh:
    Run this in terminal to execute codeI_negneg_optimisedsolve.py

- - code2_toggle_combine.py:
    Since codeI_negneg_optimisedsolve.py outputs separate files for each beta_x value, indexed by 'betaindex', run this file to combine all individual outputs. The corresponding new combined files will be named with '_final': 'Toggle_SteadyStates_final.npz', 'Toggle_Paretos_Sens1_final.npz', 'Toggle_Paretos_Sens2_final.npz', 'Toggle_Paretos_Param1_final.npz', 'Toggle_Paretos_Param2_final.npz'. 

- - code3_PlotEquilibria.py:
    Excecute this to plot the two sets of steady states. Bifurcation occurs in locations of the plot where the two steady states are different. 

- - code4_ParetosInSensAndParamSpace_SS1.py:
    Execute this to plot Pareto fronts and their parameter values belonging to the first of our pair of steady states. 

- - code5_ParetosInSensAndParamSpace_SS2.py:
    Execute this to plot Pareto fronts and their parameter values belonging to the seconds of our pair of steady states.


-----------------------------------------


- FeedbackDoubleNegative_AdjustableLeak: 
  Sensitivity analysis of double-positive feedback loop. The user is able to tweak the model leak level in codeI_dpos_optimisedsolve.py.

- - codeI_dpos_optimisedsolve.py: 
    This file defines the douple positive feedback system and sets up the grid search. The grid search is performed over three parameters: beta_x, beta_y, n. For each beta_x, indexed by 'betaindex', a full sweep is performed on beta_y and n. Each full sweep outputs the two sets of steady states in file 'dpos_steadystates' + str(betaindex) + '.npz'. For each of the two steady states, their corresponding Pareto fronts are contained in output files: 'dpos_Paretos_Sens1' + str(betaindex) + '.npz' and 'dpos_Paretos_Sens2' + str(betaindex) + '.npz' respectively. The respective paramter combinatiosn of these pareto fronts are contained in output files: 'dpos_Paretos_Params1' + str(betaindex) + '.npz' and 'dpos_Paretos_Params2' + str(betaindex) + '.npz'.

- - submit.sh:
    Run this in terminal to execute codeI_dpos_optimisedsolve.py

- - code2_toggle_combine.py:
    Since codeI_dpos_optimisedsolve.py outputs separate files for each beta_x value, indexed by 'betaindex', run this file to combine all individual outputs. The corresponding new combined files will be named with '_final': 'dpos_SteadyStates_final.npz', 'dpos_Paretos_Sens1_final.npz', 'dpos_Paretos_Sens2_final.npz', 'dpos_Paretos_Param1_final.npz', 'dpos_Paretos_Param2_final.npz'. 

- - code3_PlotEquilibria.py:
    Excecute this to plot the two sets of steady states. Bifurcation occurs in locations of the plot where the two steady states are different. 

- - code4_ParetosInSensAndParamSpace_SS1.py:
    Execute this to plot Pareto fronts and their parameter values belonging to the first of our pair of steady states. 

- - code5_ParetosInSensAndParamSpace_SS2.py:
    Execute this to plot Pareto fronts and their parameter values belonging to the seconds of our pair of steady states.


-----------------------------------------


- Circuit6B:
  This folder contains analysis for sensitivity of the circuit in Figure 6B of the paper.

- - code1_optimisedsolve.py:
    This file defines the circuit and sets up the grid search. The grid search is performed over three parameters: beta_x, beta_y, n. For each beta_x, indexed by 'betaindex', a full sweep is performed on beta_y and n.

- - submit.sh:
    Run this to execute code1_optimisedsolve.py

- - code2_combine.py
    Since code1_optimisedsolve.py outputs separate files for each beta_x value, indexed by 'betaindex', run this file to combine all individual outputs.

- - code3_plot.py:
    Run this to plot resultant Pareto fronts and their parameter value combinations. 


-----------------------------------------


- Circuit7D:
  This folder contains analysis for sensitivity of the circuit in Figure 7D of the paper.

- - code1_optimisedsolve.py:
    This file defines the circuit and sets up the grid search. The grid search is performed over three parameters: beta_x, beta_y, n. For each beta_x, indexed by 'betaindex', a full sweep is performed on beta_y and n.

- - submit.sh:
    Run this to execute code1_optimisedsolve.py

- - code2_combine.py
    Since code1_optimisedsolve.py outputs separate files for each beta_x value, indexed by 'betaindex', run this file to combine all individual outputs.

- - code3_plot.py:
    Run this to plot resultant Pareto fronts and their parameter value combinations. 


-----------------------------------------


- AllParetoPlots:
  Contains sensitivity plots for each circuit architecture and leak level.
