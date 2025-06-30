# Combines files from code 1

import numpy as np
from paretoset import paretoset



nfiles = 1000

xss1_final = np.empty((0,1))
yss1_final = np.empty((0,1))

paretoset_Sens1Pair1_combined  = np.empty((0, 2))
paretoset_Sens1Pair2_combined  = np.empty((0, 2))
paretoset_Sens1Pair3_combined  = np.empty((0, 2))
paretoset_Sens1Pair4_combined  = np.empty((0, 2))
paretoset_Sens1Pair5_combined  = np.empty((0, 2))
paretoset_Sens1Pair6_combined  = np.empty((0, 2))
paretoset_Sens1Pair7_combined  = np.empty((0, 2))
paretoset_Sens1Pair8_combined  = np.empty((0, 2))
paretoset_Sens1Pair9_combined  = np.empty((0, 2))
paretoset_Sens1Pair10_combined = np.empty((0, 2))
paretoset_Sens1Pair11_combined = np.empty((0, 2))
paretoset_Sens1Pair12_combined = np.empty((0, 2))
paretoset_Sens1Pair13_combined = np.empty((0, 2))
paretoset_Sens1Pair14_combined = np.empty((0, 2))
paretoset_Sens1Pair15_combined = np.empty((0, 2))



paretoset_Sens1mask1_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask2_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask3_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask4_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask5_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask6_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask7_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask8_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask9_Param_combined  = np.empty((0, 3))
paretoset_Sens1mask10_Param_combined = np.empty((0, 3))
paretoset_Sens1mask11_Param_combined = np.empty((0, 3))
paretoset_Sens1mask12_Param_combined = np.empty((0, 3))
paretoset_Sens1mask13_Param_combined = np.empty((0, 3))
paretoset_Sens1mask14_Param_combined = np.empty((0, 3))
paretoset_Sens1mask15_Param_combined = np.empty((0, 3))



for ifile in range(nfiles):
  print('File ' + str(ifile))
  
  filename0 = 'posneg_steadystates' + str(ifile) + '.npz'
  filename1 = 'posneg_Paretos_Sens1' + str(ifile) + '.npz'
  filename2 = 'posneg_Paretos_Params1' + str(ifile) + '.npz'
  
  fsteadystate = np.load(filename0, allow_pickle=True)
  fsenspair1 = np.load(filename1, allow_pickle=True)
  fparams1 = np.load(filename2, allow_pickle=True)
 
  xss1_final = np.vstack((xss1_final , fsteadystate['xss1']))
  yss1_final = np.vstack((yss1_final , fsteadystate['yss1']))
  
  paretoset_Sens1Pair1_combined       = np.vstack((paretoset_Sens1Pair1_combined      , fsenspair1['paretoset_Sens1Pair1']))
  paretoset_Sens1mask1_Param_combined = np.vstack((paretoset_Sens1mask1_Param_combined, fparams1['paretoset_Sens1mask1_Param']))

  paretoset_Sens1Pair2_combined       = np.vstack((paretoset_Sens1Pair2_combined      , fsenspair1['paretoset_Sens1Pair2']))
  paretoset_Sens1mask2_Param_combined = np.vstack((paretoset_Sens1mask2_Param_combined, fparams1['paretoset_Sens1mask2_Param']))

  paretoset_Sens1Pair3_combined       = np.vstack((paretoset_Sens1Pair3_combined      , fsenspair1['paretoset_Sens1Pair3']))
  paretoset_Sens1mask3_Param_combined = np.vstack((paretoset_Sens1mask3_Param_combined, fparams1['paretoset_Sens1mask3_Param']))

  paretoset_Sens1Pair4_combined       = np.vstack((paretoset_Sens1Pair4_combined      , fsenspair1['paretoset_Sens1Pair4']))
  paretoset_Sens1mask4_Param_combined = np.vstack((paretoset_Sens1mask4_Param_combined, fparams1['paretoset_Sens1mask4_Param']))

  paretoset_Sens1Pair5_combined       = np.vstack((paretoset_Sens1Pair5_combined      , fsenspair1['paretoset_Sens1Pair5']))
  paretoset_Sens1mask5_Param_combined = np.vstack((paretoset_Sens1mask5_Param_combined, fparams1['paretoset_Sens1mask5_Param']))

  paretoset_Sens1Pair6_combined       = np.vstack((paretoset_Sens1Pair6_combined      , fsenspair1['paretoset_Sens1Pair6']))
  paretoset_Sens1mask6_Param_combined = np.vstack((paretoset_Sens1mask6_Param_combined, fparams1['paretoset_Sens1mask6_Param']))

  paretoset_Sens1Pair7_combined       = np.vstack((paretoset_Sens1Pair7_combined      , fsenspair1['paretoset_Sens1Pair7']))
  paretoset_Sens1mask7_Param_combined = np.vstack((paretoset_Sens1mask7_Param_combined, fparams1['paretoset_Sens1mask7_Param']))

  paretoset_Sens1Pair8_combined       = np.vstack((paretoset_Sens1Pair8_combined      , fsenspair1['paretoset_Sens1Pair8']))
  paretoset_Sens1mask8_Param_combined = np.vstack((paretoset_Sens1mask8_Param_combined, fparams1['paretoset_Sens1mask8_Param']))

  paretoset_Sens1Pair9_combined       = np.vstack((paretoset_Sens1Pair9_combined      , fsenspair1['paretoset_Sens1Pair9']))
  paretoset_Sens1mask9_Param_combined = np.vstack((paretoset_Sens1mask9_Param_combined, fparams1['paretoset_Sens1mask9_Param']))

  paretoset_Sens1Pair10_combined       = np.vstack((paretoset_Sens1Pair10_combined      , fsenspair1['paretoset_Sens1Pair10']))
  paretoset_Sens1mask10_Param_combined = np.vstack((paretoset_Sens1mask10_Param_combined, fparams1['paretoset_Sens1mask10_Param']))

  paretoset_Sens1Pair11_combined       = np.vstack((paretoset_Sens1Pair11_combined      , fsenspair1['paretoset_Sens1Pair11']))
  paretoset_Sens1mask11_Param_combined = np.vstack((paretoset_Sens1mask11_Param_combined, fparams1['paretoset_Sens1mask11_Param']))

  paretoset_Sens1Pair12_combined       = np.vstack((paretoset_Sens1Pair12_combined      , fsenspair1['paretoset_Sens1Pair12']))
  paretoset_Sens1mask12_Param_combined = np.vstack((paretoset_Sens1mask12_Param_combined, fparams1['paretoset_Sens1mask12_Param']))

  paretoset_Sens1Pair13_combined       = np.vstack((paretoset_Sens1Pair13_combined      , fsenspair1['paretoset_Sens1Pair13']))
  paretoset_Sens1mask13_Param_combined = np.vstack((paretoset_Sens1mask13_Param_combined, fparams1['paretoset_Sens1mask13_Param']))

  paretoset_Sens1Pair14_combined       = np.vstack((paretoset_Sens1Pair14_combined      , fsenspair1['paretoset_Sens1Pair14']))
  paretoset_Sens1mask14_Param_combined = np.vstack((paretoset_Sens1mask14_Param_combined, fparams1['paretoset_Sens1mask14_Param']))

  paretoset_Sens1Pair15_combined       = np.vstack((paretoset_Sens1Pair15_combined      , fsenspair1['paretoset_Sens1Pair15']))
  paretoset_Sens1mask15_Param_combined = np.vstack((paretoset_Sens1mask15_Param_combined, fparams1['paretoset_Sens1mask15_Param']))



# Run Pareto tool with minimisation setting to get a mask.

Sens1mask1_final = paretoset(paretoset_Sens1Pair1_combined, sense=["min", "min"])
paretoset_Sens1Pair1_final = paretoset_Sens1Pair1_combined[Sens1mask1_final]

Sens1mask2_final = paretoset(paretoset_Sens1Pair2_combined, sense=["min", "min"])
paretoset_Sens1Pair2_final = paretoset_Sens1Pair2_combined[Sens1mask2_final]

Sens1mask3_final = paretoset(paretoset_Sens1Pair3_combined, sense=["min", "min"])
paretoset_Sens1Pair3_final = paretoset_Sens1Pair3_combined[Sens1mask3_final]

Sens1mask4_final = paretoset(paretoset_Sens1Pair4_combined, sense=["min", "min"])
paretoset_Sens1Pair4_final = paretoset_Sens1Pair4_combined[Sens1mask4_final]

Sens1mask5_final = paretoset(paretoset_Sens1Pair5_combined, sense=["min", "min"])
paretoset_Sens1Pair5_final = paretoset_Sens1Pair5_combined[Sens1mask5_final]

Sens1mask6_final = paretoset(paretoset_Sens1Pair6_combined, sense=["min", "min"])
paretoset_Sens1Pair6_final = paretoset_Sens1Pair6_combined[Sens1mask6_final]

Sens1mask7_final = paretoset(paretoset_Sens1Pair7_combined, sense=["min", "min"])
paretoset_Sens1Pair7_final = paretoset_Sens1Pair7_combined[Sens1mask7_final]

Sens1mask8_final = paretoset(paretoset_Sens1Pair8_combined, sense=["min", "min"])
paretoset_Sens1Pair8_final = paretoset_Sens1Pair8_combined[Sens1mask8_final]

Sens1mask9_final = paretoset(paretoset_Sens1Pair9_combined, sense=["min", "min"])
paretoset_Sens1Pair9_final = paretoset_Sens1Pair9_combined[Sens1mask9_final]

Sens1mask10_final = paretoset(paretoset_Sens1Pair10_combined, sense=["min", "min"])
paretoset_Sens1Pair10_final = paretoset_Sens1Pair10_combined[Sens1mask10_final]

Sens1mask11_final = paretoset(paretoset_Sens1Pair11_combined, sense=["min", "min"])
paretoset_Sens1Pair11_final = paretoset_Sens1Pair11_combined[Sens1mask11_final]

Sens1mask12_final = paretoset(paretoset_Sens1Pair12_combined, sense=["min", "min"])
paretoset_Sens1Pair12_final = paretoset_Sens1Pair12_combined[Sens1mask12_final]

Sens1mask13_final = paretoset(paretoset_Sens1Pair13_combined, sense=["min", "min"])
paretoset_Sens1Pair13_final = paretoset_Sens1Pair13_combined[Sens1mask13_final]

Sens1mask14_final = paretoset(paretoset_Sens1Pair14_combined, sense=["min", "min"])
paretoset_Sens1Pair14_final = paretoset_Sens1Pair14_combined[Sens1mask14_final]

Sens1mask15_final = paretoset(paretoset_Sens1Pair15_combined, sense=["min", "min"])
paretoset_Sens1Pair15_final = paretoset_Sens1Pair15_combined[Sens1mask15_final]



# Save collection of steady states
print("Saving steady state sets... in progress")

np.savez('posneg_SteadyStates_final.npz',
xss1_final = xss1_final,
yss1_final = yss1_final)

print("Saving steady state sets... complete")






# Save tables of Pareto points for each sensitivity pair
print("Saving Pareto points in sensitivity space... in progress")

np.savez('posneg_Paretos_Sens1_final.npz',
paretoset_Sens1Pair1_final  = paretoset_Sens1Pair1_final,
paretoset_Sens1Pair2_final  = paretoset_Sens1Pair2_final,
paretoset_Sens1Pair3_final  = paretoset_Sens1Pair3_final,
paretoset_Sens1Pair4_final  = paretoset_Sens1Pair4_final,
paretoset_Sens1Pair5_final  = paretoset_Sens1Pair5_final,
paretoset_Sens1Pair6_final  = paretoset_Sens1Pair6_final,
paretoset_Sens1Pair7_final  = paretoset_Sens1Pair7_final,
paretoset_Sens1Pair8_final  = paretoset_Sens1Pair8_final,
paretoset_Sens1Pair9_final  = paretoset_Sens1Pair9_final,
paretoset_Sens1Pair10_final = paretoset_Sens1Pair10_final,
paretoset_Sens1Pair11_final = paretoset_Sens1Pair11_final,
paretoset_Sens1Pair12_final = paretoset_Sens1Pair12_final,
paretoset_Sens1Pair13_final = paretoset_Sens1Pair13_final,
paretoset_Sens1Pair14_final = paretoset_Sens1Pair14_final,
paretoset_Sens1Pair15_final = paretoset_Sens1Pair15_final)

print("Saving Pareto points in sensitivity space...complete")



# __________________ CORRESPONDING PARETO FRONTS IN PARAMETER SPACE ____________________

# Get the corresponding pareto fronts in parameter space

print("Obtaining Pareto points in parameter space... in progress")

paretoset_Sens1mask1_Param_final  = paretoset_Sens1mask1_Param_combined[Sens1mask1_final]
paretoset_Sens1mask2_Param_final  = paretoset_Sens1mask2_Param_combined[Sens1mask2_final]
paretoset_Sens1mask3_Param_final  = paretoset_Sens1mask3_Param_combined[Sens1mask3_final]
paretoset_Sens1mask4_Param_final  = paretoset_Sens1mask4_Param_combined[Sens1mask4_final]
paretoset_Sens1mask5_Param_final  = paretoset_Sens1mask5_Param_combined[Sens1mask5_final]
paretoset_Sens1mask6_Param_final  = paretoset_Sens1mask6_Param_combined[Sens1mask6_final]
paretoset_Sens1mask7_Param_final  = paretoset_Sens1mask7_Param_combined[Sens1mask7_final]
paretoset_Sens1mask8_Param_final  = paretoset_Sens1mask8_Param_combined[Sens1mask8_final]
paretoset_Sens1mask9_Param_final  = paretoset_Sens1mask9_Param_combined[Sens1mask9_final]
paretoset_Sens1mask10_Param_final = paretoset_Sens1mask10_Param_combined[Sens1mask10_final]
paretoset_Sens1mask11_Param_final = paretoset_Sens1mask11_Param_combined[Sens1mask11_final]
paretoset_Sens1mask12_Param_final = paretoset_Sens1mask12_Param_combined[Sens1mask12_final]
paretoset_Sens1mask13_Param_final = paretoset_Sens1mask13_Param_combined[Sens1mask13_final]
paretoset_Sens1mask14_Param_final = paretoset_Sens1mask14_Param_combined[Sens1mask14_final]
paretoset_Sens1mask15_Param_final = paretoset_Sens1mask15_Param_combined[Sens1mask15_final]

print("Obtaining Pareto points in parameter space... complete")


# Save the arrays

print("Saving Pareto points in parameter space... in progress")

np.savez('posneg_Paretos_Param1_final.npz', 
paretoset_Sens1mask1_Param_final  = paretoset_Sens1mask1_Param_final,
paretoset_Sens1mask2_Param_final  = paretoset_Sens1mask2_Param_final,
paretoset_Sens1mask3_Param_final  = paretoset_Sens1mask3_Param_final,
paretoset_Sens1mask4_Param_final  = paretoset_Sens1mask4_Param_final,
paretoset_Sens1mask5_Param_final  = paretoset_Sens1mask5_Param_final,
paretoset_Sens1mask6_Param_final  = paretoset_Sens1mask6_Param_final,
paretoset_Sens1mask7_Param_final  = paretoset_Sens1mask7_Param_final,
paretoset_Sens1mask8_Param_final  = paretoset_Sens1mask8_Param_final,
paretoset_Sens1mask9_Param_final  = paretoset_Sens1mask9_Param_final,
paretoset_Sens1mask10_Param_final = paretoset_Sens1mask10_Param_final,
paretoset_Sens1mask11_Param_final = paretoset_Sens1mask11_Param_final,
paretoset_Sens1mask12_Param_final = paretoset_Sens1mask12_Param_final,
paretoset_Sens1mask13_Param_final = paretoset_Sens1mask13_Param_final,
paretoset_Sens1mask14_Param_final = paretoset_Sens1mask14_Param_final,
paretoset_Sens1mask15_Param_final = paretoset_Sens1mask15_Param_final)

print("Saving Pareto points in parameter space... complete")

#_______________________________________________________________________________________
